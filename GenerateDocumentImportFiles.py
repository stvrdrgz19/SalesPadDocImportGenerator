import pandas as pd
import utils
from classes.customers import Customer
from classes.items import Items

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

document_count = 12
item_num_range = [1, 5]
date_range = ["2022-10-18", "2023-10-18"]
freight_range = [0, 0, 100]
discount_range = [0, 0, 100]
qty_range = [1, 5]
warehouses = warehouse_list
items = Items.get_item_list()
has_trend = False
show_graph = False

for customer in customers:
    utils.generate_document_import(
        customer,
        document_count,
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