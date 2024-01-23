import pandas as pd
import document_import_generation as dig
from utils import DBType, get_customers, get_items, combine_spreadsheets, get_items_cost_price

db_type = DBType.TWO

customers = get_customers(db_type)
# customers = ['ALYSSAAMB000061']
# customers = ['ALYSSAAMB000061', 'PAULBYRNE000062', 'DOUGLASLE000063']
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
    'QuantityBO',
    'MarginCost'
])

document_count_range = [40, 50]
item_num_range = [1, 5]
date_range = ["2022-01-01", "2024-01-08"]
freight_range = [0, 0, 100]
discount_range = [0, 0, 100]
qty_range = [1, 5]
warehouses = ['WAREHOUSE']
# items = get_items(db_type)
items = get_items_cost_price(db_type=db_type, uofm='Each')
has_trend = True
show_graph = False

for customer in customers:
    dig.generate_document_import(
        customer,
        document_count_range,
        item_num_range,
        date_range,
        freight_range,
        discount_range,
        qty_range,
        warehouses,
        items,
        df,
        has_trend,
        show_graph
    )

combine_spreadsheets(True)