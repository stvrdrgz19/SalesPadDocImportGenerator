import random
import pyodbc
import matplotlib.pyplot as plt
from collections import Counter
import json
import pandas as pd
from classes.items import Items
from enum import Enum
import os

class DBType(Enum):
    TWO = 1
    TWOMB = 2

class DocTypes(Enum):
    Invoice = 1
    Return = 2
    Order = 3

class SettingTypes(Enum):
    Document = 1
    Import = 2

class Trends(Enum):
    Increase = 1
    Decrease = 2
    UpDown = 3
    DownUp = 4
    Wave = 5
    Seasonal = 6
    Churned = 7

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

def process_excel_files(df, documents, split):
    if split:
        document_count = len(documents)
        document_split_count = round(document_count*.75)
        generate_excel_files(df, documents[:document_split_count], "pre_cost_update_documents")
        generate_excel_files(df, documents[document_split_count+1:], "post_cost_update_documents")
    else:
        generate_excel_files(df, documents, "documents")

def generate_excel_files(df, documents, file_name):
    file_path = f"output/{file_name}.xlsx"
    for document in documents:
        for line in document.lines:
            new_row = {
                'DocNum': document.doc_num,
                'DocType': document.doc_type,
                'CustomerNum': document.customer_num,
                'DocID': document.doc_id,
                'DocDate': document.doc_date,
                'Freight': document.freight,
                'Discount': document.discount,
                'Warehouse': document.warehouse,
                'LineNum': line.line_num,
                'ComponentSeq': line.component_seq_num,
                'ItemNum': line.item_num,
                'Quantity': line.quantity,
                'Queue': document.queue,
                'QuantityBO': line.quantity_bo,
                'UofM' : line.uofm
            }
            
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(file_path, index = False, sheet_name = "Sheet1")
    print(f"Document generated at '{file_path}'")

def combine_spreadsheets(delete: bool = False) -> None:
    path = 'output'
    dfs = []
    output_file = f'{path}/Combined_Import.xlsx'

    # remove existing combined document if exists
    delete_file(output_file)

    for file_name in os.listdir(path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(path, file_name)

            # read the xlsx file into a dataframe
            df = pd.read_excel(file_path)

            # append the data to the dfs list
            dfs.append(df)
            if delete:
                delete_file(file_path)

    combined_df = pd.concat(dfs, ignore_index=True)

    # output the combined data to a new xlsx sheet
    combined_df.to_excel(output_file, index=False, sheet_name="Sheet1")
    print(f"Spreadsheets combined to: {output_file}")

def delete_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"File '{file_path}' does not exist.")

def get_sql_connection(server, database, username, password):
    driver = '{ODBC Driver 17 for SQL Server}'
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    return pyodbc.connect(connection_string)

def get_items(db_type: DBType) -> list:
    conn = get_sql_connection('SRODRIGUEZ\SQLSERVER2016', db_type.name, 'sa', 'sa')
    cursor = conn.cursor()

    if db_type == DBType.TWO:
        count = 556
    else:
        count = 268

    sql = f"""
        SELECT 
            ITEMNMBR,
            CASE 
                WHEN ITEMTYPE = 1 THEN 'Inventory'
                WHEN ITEMTYPE = 3 THEN 'Kit'
                WHEN ITEMTYPE = 5 THEN 'Service'
            END AS ItemTypeLabel
        FROM IV00101
        WHERE DEX_ROW_ID > {count};
        """
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    item_list = []
    for row in rows:
        item = Items(*row)
        item_list.append(item)

    return item_list

def get_customers(db_type: DBType) -> list:
    conn = get_sql_connection('SRODRIGUEZ\SQLSERVER2016', db_type.name, 'sa', 'sa')
    cursor = conn.cursor()

    sql = 'SELECT CUSTNMBR FROM RM00101 WHERE DEX_ROW_ID > 104'

    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    customer_list = [', '.join(str(item).strip() for item in row) for row in rows]

    return customer_list

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

def get_doc_num_start_from_type(type):
    if type == 'ORDER':
        return 'ORDST'
    if type == 'INVOICE':
        return 'STDINV'
    if type == 'RETURN':
        return 'RTN'
    else:
        return 'ERROR'

def get_next_doc_num(type, num_type):
    doc_num_start = get_doc_num_start_from_type(type)
    doc_num = doc_num_start.ljust(15, '0')
    next_doc_num = str(get_next_num(num_type))
    trimmed_doc_num = doc_num[:-len(next_doc_num)]
    end_doc_num = trimmed_doc_num + next_doc_num
    return end_doc_num

def get_next_num(type: SettingTypes) -> str:
    with open("configuration/settings.json", "r") as file:
        data = json.load(file)

    if type == SettingTypes.Document:
        next_num = data["next_doc_num"]
        data["next_doc_num"] = next_num + 1

    if type == SettingTypes.Import:
        next_num = data["next_generated_import_num"]
        data["next_generated_import_num"] = next_num + 1

    with open("configuration/settings.json", "w") as file:
        json.dump(data, file, indent = 4)

    return next_num
