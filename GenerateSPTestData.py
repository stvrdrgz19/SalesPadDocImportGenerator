import pandas as pd
from datetime import datetime
import random
import re

def get_date_from_range(startDate, endDate):
    date_range = pd.date_range(start=startDate, end=endDate)
    indx = random.sample(range(len(date_range)), 1)
    date_obj = date_range[indx]
    date_string = date_obj.strftime('%Y-%m-%d')
    pattern = r"['\"](.*?)['\"]"
    date_match = re.findall(pattern, str(date_string))
    return date_match[0]

def get_freightDiscount(min_val, max_val, threshold):
    perc = round(random.uniform(0, 100), 0)

    if perc < threshold:
        return 0.00
    
    else:
        return round(random.uniform(min_val, max_val), 2)

count = 0
documentsToGenerate = 200
startingDocNum = 10200
docType = 'ORDER'
customers = [
    'AARONFIT0001',
    'NORTHERN0001',
    'GREENWAY0001',
    'ATMORERE0001',
    'BLUEYOND0001',
    'WESTSIDE0001',
    'NORTHCOL0001',
    'CONTOSOL0001',
    'HOMEFURN0001',
    'CELLULAR0001',
    'FRANCHIS0001',
    'ASTORSUI0001',
    'ADAMPARK0001',
    'NETWORKS0001',
    'COHOWINE0001',
    'UNIFIEDW0001',
    'MARGIEST0001',
    'DIRECTMA0001',
    'MIDCITYH0001',
    'LASERMES0001'
]
docID = 'STDORD'
min_qty = 1
max_qty = 10
warehouse = 'WAREHOUSE'
lineNum = '16384'
componentSeq = 0
items = [
    '100XLG',
    '128 SDRAM',
    '3-C2804A',
    '333PROC',
    '4-E5930A',
    'CORDG',
    'HA100G',
    'HDWR-PNL-0001',
    'HDWR-SRG-0001',
    'OM08620',
    'OM08640',
    'OM08670',
    'PHON-ATT-0712',
    'PHON-FGD-0001',
    'PHON-FGS-0002',
    'PHSY-DEL-0001',
    'PHSY-STD-0001',
    'SOFT-PHM-0001',
    'CBA100',
    '8.4HD'
]
queue = 'ONE'

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

while count < documentsToGenerate:
    # get next doc num
    nextDocNum = startingDocNum + count

    # pick a random customer from the list
    selectedCustomer = random.choice(customers)

    # get a random date from the range
    selectedDate = get_date_from_range("2021-09-09", "2023-10-06")

    # get random freight and doscunt from range
    selectedFreight = get_freightDiscount(5, 25, 66.6)
    selectedDiscount = get_freightDiscount(5, 25, 66.6)

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
        'DocDate': selectedDate,
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
df.to_excel('SDImport.xlsx', index = False, sheet_name= 'Sheet1')