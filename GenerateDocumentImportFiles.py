import pandas as pd
import random
import utils
from classes.dates import get_dates_with_trends
from classes.customers import Customer
from classes.items import Items

def generate_document_import(customer, count, starting_doc_num, item_num_range, date_range, freight_range, discount_range, qty_range, warehouses, items, df):
    file_name = f"{customer.number}_{customer.trend}_{customer.scenario}.xlsx"
    i = 0
    base_line_num = 16384
    backorder_qty = 0

    dates = get_dates_with_trends(date_range[0], date_range[1], customer.trend, count)
    utils.visualize_data(dates, customer.trend)

    if customer.scenario == "OrderInvoicePartial" or customer.scenario == "OrderInvoiceSplit":
        supportPartial = True
    else:
        supportPartial = False

    boQtyPercentThreshold = 75.5

    if customer.scenario == "Invoice":
        queue = "NEW INVOICE"
        doc_type = "INVOICE"
        doc_id = "STDINV"
    else:
        queue = "NEW ORDER"
        doc_type = "ORDER"
        doc_id = "STDORD"

    for date in dates:
        doc_num = starting_doc_num + i
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
                'CustomerNum': customer.number,
                'DocID': doc_id,
                'DocDate': date,
                'Freight': freight,
                'Discount': discount,
                'Warehouse': warehouse,
                'LineNum': base_line_num * num_of_rows,
                'ComponentSeq': 0,
                'ItemNum': item.number,
                'Quantity': qty,
                'Queue': queue,
                'QuantityBO': backorder_qty
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        i += 1
    
    starting_doc_num += count
    df.to_excel(f"output/{file_name}", index = False, sheet_name = "Sheet1")

customers = Customer.get_customer_list()
warehouse_list = ['WAREHOUSE']
df = pd.DataFrame(columns=[
    'DocNum',
    'DocType',
    'CustomerNum',
    'DocID',
    'DocDate',
    'Freight',
    'Discount',
    'Warehouse',
    'LineNum',
    'ComponentSeq',
    'ItemNum',
    'Quantity',
    'Queue',
    'QuantityBO'
])

for customer in customers:
    generate_document_import(customer, 1000, 10000, [3, 5], ["2021-10-10", "2023-10-10"], [5, 25, 66.6], [5, 25, 75.7], [3, 10], warehouse_list, Items.get_item_list(), df)

# doc_count_per_customer = 1000
# item_num_min = 3
# item_num_max = 5
# starting_doc_num = 20000
# start_date = '2021-10-11'
# end_date = '2023-10-11'
# freight_min = 5
# freight_max = 25
# freight_percent = 75.5
# discount_min = 5
# discount_max = 20
# discount_percent = 66.6
# qty_min = 3
# qty_max = 10
# warehouse_list = ['WAREHOUSE']
# item_list = Items.get_item_list()

# for customer in Customer.get_customer_list():
#     file_name = f"{customer.number}_{customer.trend}_{customer.scenario}.xlsx"
#     count = 0
#     starting_line_num = 16384
#     df = pd.DataFrame(columns=[
#         'DocNum',
#         'DocType',
#         'CustomerNum',
#         'DocID',
#         'DocDate',
#         'Freight',
#         'Discount',
#         'Warehouse',
#         'LineNum',
#         'ComponentSeq',
#         'ItemNum',
#         'Quantity',
#         'Queue',
#         'QuantityBO'
#     ])
#     boQty = 0

#     if customer.scenario == "OrderInvoicePartial" or customer.scenario == "OrderInvoiceSplit":
#         supportPartial = True
#     else:
#         supportPartial = False

#     boQtyPercentThreshold = 75.5

#     if customer.scenario == "Invoice":
#         queue = "NEW INVOICE"
#         doc_type = "INVOICE"
#         doc_id = "STDINV"
#     else:
#         queue = "NEW ORDER"
#         doc_type = "ORDER"
#         doc_id = "STDORD"

#     dates = get_dates_with_trends(start_date, end_date, customer.trend, doc_count_per_customer)

#     for date in dates:
#         doc_num = starting_doc_num + count
#         freight = utils.get_freight_or_discount(freight_min, freight_max, freight_percent, 2)
#         discount = utils.get_freight_or_discount(discount_min, discount_max, discount_percent, 2)
#         warehouse = random.choice(warehouse_list)
#         num_of_items = round(random.uniform(item_num_min, item_num_max), 0)
#         num_of_rows = 0
#         while num_of_rows < num_of_items:
#             num_of_rows += 1
#             item = random.choice(item_list)
#             qty = round(random.uniform(qty_min, qty_max), 0)
#             if (supportPartial):
#                 if item.type == "Inventory":
#                     boQty = utils.get_freight_or_discount(0, qty, boQtyPercentThreshold, 0)
#                 else:
#                     boQty = 0

#             new_row = {
#                 'DocNum': doc_num,
#                 'DocType': doc_type,
#                 'CustomerNum': customer.number,
#                 'DocID': doc_id,
#                 'DocDate': date,
#                 'Freight': freight,
#                 'Discount': discount,
#                 'Warehouse': warehouse,
#                 'LineNum': starting_line_num * num_of_rows,
#                 'ComponentSeq': 0,
#                 'ItemNum': item.number,
#                 'Quantity': qty,
#                 'Queue': queue,
#                 'QuantityBO': boQty
#             }

#             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#         count += 1
    
#     starting_doc_num += doc_count_per_customer
#     df.to_excel(f"output/{file_name}", index = False, sheet_name = "Sheet1")