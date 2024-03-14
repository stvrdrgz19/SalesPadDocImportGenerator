import pandas as pd
import document_import_generation as dig
from utils import DBType, get_customers, get_items, process_excel_files
from classes.document import Document

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
    'UofM'
])

document_count_range = [25, 50]
item_num_range = [1, 5]
date_range = ["2022-01-01", "2024-03-13"]
freight_range = [0, 50, 95]
discount_range = [0, 50, 85]
qty_range = [1, 5]
warehouses = ['WAREHOUSE']
items = get_items(db_type)
has_trend = True
show_graph = False

documents_per_customer = []
documents = []

for customer in customers:
    documents_per_customer.append(dig.generate_document_import(
        customer
        ,document_count_range
        ,item_num_range
        ,date_range
        ,freight_range
        ,discount_range
        ,qty_range
        ,warehouses
        ,items
        ,df
        ,has_trend
        ,show_graph
    ))

for document_group in documents_per_customer:
    for doc in document_group:
        documents.append(doc)

sorted_documents = sorted(documents, key=Document.sort_by_date)
document_count = len(sorted_documents)

process_excel_files(df, sorted_documents, True)
process_excel_files(df, sorted_documents, False)
