import pandas as pd
import document_import_generation as dig
from utils import DBType, get_customers, get_items, get_items_with_details, process_excel_files, df
from classes.document import Document

db_type = DBType.TWO

customers = get_customers(db_type)
# customers = ['ALYSSAAMB000061']
# customers = ['ALYSSAAMB000061', 'PAULBYRNE000062', 'DOUGLASLE000063']

document_count_range = [25, 70]
item_num_range = [1, 5]
date_range = ["2022-01-01", "2024-04-11"]
freight_range = [0, 50, 95]
discount_range = [5, 25, 85]
markdown_range = [5, 25, 85]
qty_range = [1, 5]
warehouses = ['WAREHOUSE']
items = get_items_with_details(db_type)
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
        ,markdown_range
        ,qty_range
        ,warehouses
        ,items
        ,has_trend
        ,show_graph
        ,db_type
    ))

for document_group in documents_per_customer:
    for doc in document_group:
        documents.append(doc)

# for document in documents:
    # lines = document.lines
    # for line in lines[:-1]:
    #     line.discount = 0

sorted_documents = sorted(documents, key=Document.sort_by_date)
# process_excel_files(df, sorted_documents, True)
process_excel_files(df, sorted_documents, False)
