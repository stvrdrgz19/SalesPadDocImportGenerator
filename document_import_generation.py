import utils
import random
import numpy as np
from classes.dates import get_dates_with_trends, get_one_date_per_month_from_range
from classes.document import Document
from classes.line import Line

def generate_document_import(customer, document_count_range, item_num_range, date_range, freight_range, discount_range, qty_range, warehouses, items, df, has_trend, show_graph):
    base_line_num = 16384
    backorder_qty = 0
    trend = random.choice([member.name for member in utils.Trends])
    scenario = utils.DocTypes.Invoice.name
    count = random.randint(document_count_range[0], document_count_range[1])
    unit_of_measures = ['Each', 'Case']

    if has_trend:
        dates = get_dates_with_trends(date_range[0], date_range[1], trend, count)
    else:
        dates = get_one_date_per_month_from_range(date_range[0], date_range[1])

    sorted_dates = np.sort(dates)

    if show_graph:
        utils.visualize_data(dates, trend)

    if scenario == "OrderInvoicePartial" or scenario == "OrderInvoiceSplit":
        supportPartial = True
    else:
        supportPartial = False

    boQtyPercentThreshold = 75.5

    if scenario == "Invoice":
        queue = "NEW INVOICE"
        doc_type = "INVOICE"
        doc_id = "STDINV"
    if scenario == "Return":
        queue = "NEW RETURN"
        doc_type = "RETURN"
        doc_id = "RTN"
    if scenario == "Order":
        queue = "NEW ORDER"
        doc_type = "ORDER"
        doc_id = "STDORD"

    documents = []

    for date in sorted_dates:
        doc_num = utils.get_next_doc_num(doc_type, utils.SettingTypes.Document)
        freight = utils.get_freight_or_discount(freight_range[0], freight_range[1], freight_range[2], 2)
        discount = utils.get_freight_or_discount(discount_range[0], discount_range[1], discount_range[2], 2)
        warehouse = random.choice(warehouses)
        num_of_items = round(random.uniform(item_num_range[0], item_num_range[1]), 0)
        num_of_rows = 0

        lines = []
        while num_of_rows < num_of_items:
            num_of_rows += 1
            item = random.choice(items)
            qty = round(random.uniform(qty_range[0], qty_range[1]), 0)
            if (supportPartial):
                if item.type == "Inventory":
                    backorder_qty = utils.get_freight_or_discount(0, qty, boQtyPercentThreshold, 0)
                else:
                    backorder_qty = 0
                    
            line = Line(
                line_num=base_line_num * num_of_rows
                ,component_seq_num=0
                ,item_num=item.number
                ,quantity=qty
                ,quantity_bo=backorder_qty
                ,uofm=random.choice(unit_of_measures)
            )
            lines.append(line)
            
        document = Document(
            doc_num=doc_num
            ,doc_type=doc_type
            ,doc_id=doc_id
            ,customer_num=customer
            ,doc_date=date
            ,warehouse=warehouse
            ,queue=queue
            ,freight=freight
            ,discount=discount
            ,lines=lines
        )
        documents.append(document)
    print(f"{customer} - {len(documents)} documents")
    return documents