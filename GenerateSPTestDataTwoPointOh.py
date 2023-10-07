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

def generate_documents(
        fileName,
        tabName,
        numberOfDocuments,
        item_num_min,
        item_num_max,
        startingDocNum,
        docType,
        docID,
        customers,
        startDate,
        endDate,
        freight_min,
        freight_max,
        freight_perc,
        discount_min,
        discount_max,
        discount_perc,
        warehouses,
        qty_min,
        qty_max,
        items,
        queues
):
    count = 0
    startingLineNum = 16384
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

    while count < numberOfDocuments:
        # set the document number
        docNum = startingDocNum + count

        # pick a customer
        customer = random.choice(customers)

        # get a random date from the range
        date = get_date_from_range(startDate, endDate)

        # get random freight and doscunt from range
        freight = get_freightDiscount(freight_min, freight_max, freight_perc)
        discount = get_freightDiscount(discount_min, discount_max, discount_perc)

        # get the warehouse
        warehouse = random.choice(warehouses)

        #determine how many lines are on the document
        numOfItems = round(random.uniform(item_num_min, item_num_max), 0)
        numOfRows = 0
        while numOfRows < numOfItems:
            numOfRows += 1
            # get random item from list
            item = random.choice(items)

            # get random quantity from range
            qty = round(random.uniform(qty_min, qty_max), 0)

            # get random queue from range
            queue = random.choice(queues)

            # create new row
            new_row = {
                'DocNum': docNum,
                'DocType': docType,
                'CustomerNum': customer,
                'DocID': docID,
                'DocDate': date,
                'Freight': freight,
                'Discount': discount,
                'Warehouse': warehouse,
                'LineNum': startingLineNum * numOfRows,
                'ComponentSeq': 0,
                'ItemNum': item,
                'Quantity': qty,
                'Queue': queue
            }

            # add new row to dataframe
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        count += 1

    # Export spreadsheet
    df.to_excel(fileName, index = False, sheet_name= tabName)

# VALUES
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

fileName = 'test.xlsx'
tabName = 'Sheet1'
numberOfDocuments = 1000
lineItemMin = 3
lineItemMax = 5
startingDocumentNum = 3000
docType = 'ORDER'
docID = 'STDORD'
startDate = '2021-09-09'
endDate = '2023-10-06'
freightMin = 5
freightMax = 25
freightPercentChance = 50.0
discountMin = 5
discountMax = 25
discountPercentChance = 66.6
warehouses = ['WAREHOUSE']
qtyMin = 1
qtyMax = 15
queues = ['ONE']

generate_documents(
    fileName,
    tabName,
    numberOfDocuments,
    lineItemMin,
    lineItemMax,
    startingDocumentNum,
    docType,
    docID,
    customers,
    startDate,
    endDate,
    freightMin,
    freightMax,
    freightPercentChance,
    discountMin,
    discountMax,
    discountPercentChance,
    warehouses,
    qtyMin,
    qtyMax,
    items,
    queues
)