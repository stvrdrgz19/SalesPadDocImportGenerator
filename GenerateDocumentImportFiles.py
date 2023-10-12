import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from CustomerClass import Customer
import items

# get a trend based off of weight inputs
def trend(count, start_weight, end_weight):
    lin_sp = np.linspace(start_weight, end_weight, count)
    return lin_sp/sum(lin_sp)

# gets a number of dates between a range based off of a trend
def get_dates(start, end, doc_count, start_weight, end_weight):
    dates = pd.date_range(start, end, freq="D")
    date_trends = np.random.choice(dates, size=doc_count, p=trend(len(dates), start_weight, end_weight))
    return date_trends

# randomly (within a threshold) determines if a document has freight/discount, as well as how much
def get_freight_or_discount(min_val, max_val, threshold, dec):
    percent = round(random.uniform(0, 100), 0)

    if percent < threshold:
        return 0
    
    else:
        return round(random.uniform(min_val, max_val), dec)

# gets multiple sets of dates between ranges and trends
def get_dates_with_trends(start_date, end_date, trend, number_of_docs):
    #format dates
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)

    #get number of days within range
    days = end - start
    number_of_days = days.days

    if trend == "UpDown" or trend == "DownUp":
        days_per_direction = timedelta(days=round(number_of_days/2))
        docs_per_direction = round(number_of_docs/2)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + timedelta(days=1)
        dates1 = get_dates(start, first_end_day, round(docs_per_direction), 1, 15)
        dates2 = get_dates(second_start_day, end, round(docs_per_direction), 15, 1)
        return np.concatenate((dates1, dates2), axis=0)
    
    if trend == "Wave":
        days_per_direction = timedelta(days=round(number_of_days/4))
        docs_per_direction = round(number_of_docs/4)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + timedelta(days=1)
        second_end_day = second_start_day + days_per_direction
        third_start_day = second_end_day + timedelta(days=1)
        third_end_day = third_start_day + days_per_direction
        fourth_start_day = third_end_day + timedelta(days=1)

        dates1 = get_dates(start, first_end_day, docs_per_direction, 1, 15)
        dates2 = get_dates(second_start_day, second_end_day, docs_per_direction, 15, 1)
        dates3 = get_dates(third_start_day, third_end_day, docs_per_direction, 1, 15)
        dates4 = get_dates(fourth_start_day, end, docs_per_direction, 15, 1)

        # concat dates in a weird way...
        dates_concat_1 = np.concatenate((dates1, dates2), axis=0)
        dates_concat_2 = np.concatenate((dates_concat_1, dates3), axis=0)
        return np.concatenate((dates_concat_2, dates4), axis=0)

    
    if trend == "Seasonal":
        days_per_direction = timedelta(days=round(number_of_days/5))
        docs_per_direction = round(number_of_docs/3)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + days_per_direction
        second_end_day = second_start_day + days_per_direction
        third_start_day = second_end_day + days_per_direction

        dates1 = get_dates(start, first_end_day, docs_per_direction, 1, 15)
        dates2 = get_dates(second_start_day, second_end_day, docs_per_direction, 1, 15)
        dates3 = get_dates(third_start_day, end, docs_per_direction, 1, 15)

        # concat dates in a weird way...
        dates_concat_1 = np.concatenate((dates1, dates2), axis=0)
        return np.concatenate((dates_concat_1, dates3), axis=0)

    if trend == "Churn":
        new_end_day = end - timedelta(days=370)
        new_days = new_end_day - start
        percent_of_days = new_days/days
        new_number_of_docs = round(number_of_docs * percent_of_days)

        dates = get_dates(start, new_end_day, new_number_of_docs, 15, 1)
        return dates

doc_count_per_customer = 1000
item_num_min = 3
item_num_max = 5
starting_doc_num = 20000
start_date = '2021-10-11'
end_date = '2023-10-11'
freight_min = 5
freight_max = 25
freight_percent = 75.5
discount_min = 5
discount_max = 20
discount_percent = 66.6
qty_min = 3
qty_max = 10
warehouse_list = ['WAREHOUSE']
item_list = items.items

for customer in Customer.get_customer_list():
    file_name = f"{customer.number}_{customer.trend}_{customer.scenario}.xlsx"
    count = 0
    starting_line_num = 16384
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
    boQty = 0

    kit_items = [
        'DCP-1001',
        'DCP-2002',
        'DCP-3003'
    ]

    service_items = [
        'SUPP-1001',
        'SUPP-2002',
        'SUPP-3003'
    ]

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

    if customer.trend == "Increase":
        dates = get_dates(start_date, end_date, 1000, 1, 15)
    elif customer.trend == "Decrease":
        dates = get_dates(start_date, end_date, 1000, 15, 1)
    else:
        dates = get_dates_with_trends(start_date, end_date, customer.trend, 1000)

    for date in dates:
        doc_num = starting_doc_num + count
        freight = get_freight_or_discount(freight_min, freight_max, freight_percent, 2)
        discount = get_freight_or_discount(discount_min, discount_max, discount_percent, 2)
        warehouse = random.choice(warehouse_list)
        num_of_items = round(random.uniform(item_num_min, item_num_max), 0)
        num_of_rows = 0
        while num_of_rows < num_of_items:
            num_of_rows += 1
            item = random.choice(item_list)
            qty = round(random.uniform(qty_min, qty_max), 0)
            if (supportPartial):
                if item not in kit_items and item not in service_items:
                    boQty = get_freight_or_discount(0, qty, boQtyPercentThreshold, 0)
                else:
                    boQty = 0
            new_row = {
                'DocNum': doc_num,
                'DocType': doc_type,
                'CustomerNum': customer.number,
                'DocID': doc_id,
                'DocDate': date,
                'Freight': freight,
                'Discount': discount,
                'Warehouse': warehouse,
                'LineNum': starting_line_num * num_of_rows,
                'ComponentSeq': 0,
                'ItemNum': item,
                'Quantity': qty,
                'Queue': queue,
                'QuantityBO': boQty
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        count += 1
    
    starting_doc_num += 1000
    df.to_excel(f"output2/{file_name}", index = False, sheet_name = "Sheet1")