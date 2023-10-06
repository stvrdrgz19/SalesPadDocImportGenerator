import pandas as pd
from datetime import datetime
import random

count = 0
startingDocNum = 10000
docType = 'INVOICE'
customers = [
    'AARONFIT0001',
    'OCTAGONM0001',
    'CENTRALI0001',
    'REDSFOOD0001',
    'PLAZAONE0001',
    'STMARYHO0001',
    'LASERMES0001',
    'JOHNSONK0001',
    'BAKERSEM0001',
    ]
docID = 'STDINV'
date_range = pd.date_range(start="2021-09-09", end="2023-10-06")
min_freight = 0.01
max_freight = 30.00
min_discount = 0.01
max_discount = 10.00
min_qty = 1
max_qty = 10
warehouse = 'WAREHOUSE'
lineNum = '16384'
componentSeq = 0
items = [
    '0XNON1',
    '0XLOT1',
    '0XSERIAL1',
    '0XKIT1'
]
queue = 'POST'

# columns headers
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
    'Queue'
])

while count < 100:
    # get next doc num
    nextDocNum = startingDocNum + count

    # pick a random customer from the list
    selectedCustomer = random.choice(customers)

    # get a random date from the range
    # date is still being sent as an object index? How to only pass date
    indx = random.sample(range(len(date_range)), 1)
    date_obj = date_range[indx]
    selectedDate = date_obj.strftime("%m/%d/%Y")

    # get random freight and doscunt from range
    selectedFreight = round(random.uniform(min_freight, max_freight), 2)
    selectedDiscount = round(random.uniform(min_discount, max_discount), 2)

    # get random item from list
    selectedItem = random.choice(items)

    # get random quantity from range
    selectedQty = round(random.uniform(min_qty, max_qty), 0)

    # create new row
    new_row = {
        'DocNum': nextDocNum,
        'DocType': docType,
        'CustomerNum': selectedCustomer,
        'DocID': docID,
        'DocDate': selectedDate.astype(str),
        'Freight': selectedFreight,
        'Discount': selectedDiscount,
        'Warehouse': warehouse,
        'LineNum': lineNum,
        'ComponentSeq': componentSeq,
        'ItemNum': selectedItem,
        'Quantity': selectedQty,
        'Queue': queue
    }

    # add new row to dataframe
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    count += 1

# Export spreadsheet
df.to_excel('output4.xlsx', index = False, sheet_name= 'Sheet1')