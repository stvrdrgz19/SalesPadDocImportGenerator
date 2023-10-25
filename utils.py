import random
import matplotlib.pyplot as plt
from collections import Counter
import json
from classes.dates import get_dates_with_trends, get_one_date_per_month_from_range
import pandas as pd

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

# randomly (within a threshold) determines if a document has freight/discount, as well as how much
def get_freight_or_discount(min_val, max_val, threshold, dec):
    percent = round(random.uniform(0, 100), 0)

    if percent < threshold:
        return 0
    
    else:
        return round(random.uniform(min_val, max_val), dec)

def visualize_data(dates, title):
    # remove duplicate dates
    unique_dates = list(set(dates))
    # sort dates
    unique_dates.sort()

    # get count per date
    count_dict = Counter(dates)
    count_list = list(count_dict.values())

    fig, ax = plt.subplots()
    ax.plot(unique_dates, count_list, label='Date Trends')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.legend()

    plt.show()

def get_next_doc_num():
    with open("configuration/settings.json", "r") as file:
        data = json.load(file)

    next_doc_num = data["next_doc_num"]
    data["next_doc_num"] = next_doc_num + 1

    with open("configuration/settings.json", "w") as file:
        json.dump(data, file, indent = 4)

    return next_doc_num

def get_next_generated_import_num():
    with open("configuration/settings.json", "r") as file:
        data = json.load(file)

    next_generated_import_num = data["next_generated_import_num"]
    data["next_generated_import_num"] = next_generated_import_num + 1

    with open("configuration/settings.json", "w") as file:
        json.dump(data, file, indent = 4)

    return next_generated_import_num

def generate_document_import(customer, count, item_num_range, date_range, freight_range, discount_range, qty_range, warehouses, items, df, has_trend, show_graph):
    # file_name = f"{customer.number}_{customer.trend}_{customer.scenario}.xlsx"
    next_generated_import_num = get_next_generated_import_num()
    file_name = f"{next_generated_import_num}_{customer.number}.xlsx"
    i = 0
    base_line_num = 16384
    backorder_qty = 0

    if has_trend:
        dates = get_dates_with_trends(date_range[0], date_range[1], customer.trend, count)
    else:
        dates = get_one_date_per_month_from_range(date_range[0], date_range[1])

    if show_graph:
        visualize_data(dates, customer.trend)

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
        doc_num = get_next_doc_num()
        freight = get_freight_or_discount(freight_range[0], freight_range[1], freight_range[2], 2)
        discount = get_freight_or_discount(discount_range[0], discount_range[1], discount_range[2], 2)
        warehouse = random.choice(warehouses)
        num_of_items = round(random.uniform(item_num_range[0], item_num_range[1]), 0)
        num_of_rows = 0
        while num_of_rows < num_of_items:
            num_of_rows += 1
            item = random.choice(items)
            qty = round(random.uniform(qty_range[0], qty_range[1]), 0)
            if (supportPartial):
                if item.type == "Inventory":
                    backorder_qty = get_freight_or_discount(0, qty, boQtyPercentThreshold, 0)
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
    
    df.to_excel(f"output/{file_name}", index = False, sheet_name = "Sheet1")