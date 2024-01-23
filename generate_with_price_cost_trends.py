import pandas as pd
import document_import_with_trends_gen as trends
from utils import DBType, get_customers, get_items_cost_price, delete_file

db_type = DBType.TWO
customers = get_customers(db_type)
items = get_items_cost_price(db_type, 'Each')
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
    'UnitPrice',
    'UnitCost',
    'Queue',
    'QuantityBO'
])

document_count_range = [40, 50]
item_num_range = [1, 5]
date_range = ["2022-01-01", "2024-01-08"]
freight_range = [0, 0, 100]
discount_range = [0, 50, 90]
qty_range = [1, 5]
warehouses = ['WAREHOUSE']
has_trend = True
show_graph = False
dfs = []
output_file = 'output/Combined_Import_Test.xlsx'

for customer in customers:
    dfs.append(trends.generate_document_import(
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
    ))

delete_file(output_file)
combined_df = pd.concat(dfs, ignore_index=True)
df_sorted = combined_df.sort_values(by=['DocDate', 'LineNum'])
# get unique list of items
exploded_df = df_sorted['ItemNum'].explode()
#   get a unique list
unique_items = exploded_df.unique().tolist()


# select some items from list at random to adjust price or cost +/-
# alter documents whose date fits within the last quarter of the provided range
df_sorted.to_excel(output_file, index=False, sheet_name='Sheet1')
print(f"Spreadsheets combined to: {output_file}")