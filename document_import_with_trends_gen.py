import utils
import random
import pandas as pd
import numpy as np
from classes.dates import get_dates_with_trends, get_one_date_per_month_from_range

def generate_document_import(customer, document_count_range, item_num_range, date_range, freight_range, discount_range, qty_range, warehouses, items, df, has_trend, show_graph):
    base_line_num = 16384
    backorder_qty = 0
    trend = random.choice([member.name for member in utils.Trends])
    scenario = utils.DocTypes.Invoice.name
    count = random.randint(document_count_range[0], document_count_range[1])

    if has_trend:
        dates = get_dates_with_trends(date_range[0], date_range[1], trend, count)
    else:
        dates = get_one_date_per_month_from_range(date_range[0], date_range[1])

    if show_graph:
        utils.visualize_data(dates, trend)

    sorted_dates = np.sort(dates)

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

    for date in sorted_dates:
        doc_num = utils.get_next_doc_num(doc_type, utils.SettingTypes.Document)
        freight = utils.get_freight_or_discount(freight_range[0], freight_range[1], freight_range[2], 2)
        discount = utils.get_freight_or_discount(discount_range[0], discount_range[1], discount_range[2], 2)
        warehouse = random.choice(warehouses)
        num_of_items = round(random.uniform(item_num_range[0], item_num_range[1]), 0)
        num_of_rows = 0
        while num_of_rows < num_of_items:
            num_of_rows += 1
            item = random.choice(items)
            qty = round(random.uniform(qty_range[0], qty_range[1]), 0)
            if (supportPartial):
                if item.type == "Inventory":
                    backorder_qty = utils.get_freight_or_discount(0, qty, boQtyPercentThreshold, 0)
                else:
                    backorder_qty = 0

            new_row = {
                'DocNum': doc_num,
                'DocType': doc_type,
                'CustomerNum': customer,
                'DocID': doc_id,
                'DocDate': date,
                'Freight': freight,
                'Discount': discount,
                'Warehouse': warehouse,
                'LineNum': base_line_num * num_of_rows,
                'ComponentSeq': 0,
                'ItemNum': item.number,
                'Quantity': qty,
                'UnitPrice': item.price,
                'UnitCost': item.cost,
                'Queue': queue,
                'QuantityBO': backorder_qty
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df