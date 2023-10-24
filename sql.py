import pandas as pd
import pyodbc
import csv

server = 'SRODRIGUEZ\SQLSERVER2016'
database = 'TWO'
username = 'sa'
password = 'sa'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print(f"Error connecting to the database {e}")
    exit()

start_date = '2022-01-01'
end_date = '2023-10-30'

sql_query = f"EXEC dbo.spcpGetSalesAndMarginMonthly @Begin_Date = '{start_date}', @End_Date = '{end_date}'"

df = pd.DataFrame(columns=[
    'year',
    'month',
    'subtotal',
    'total_cost',
    'margin_amount',
    'margin_percent'
])

try:
    cursor = conn.cursor()
    cursor.execute(sql_query)

    result = cursor.fetchall()

    output_file = 'output\SQLResults.xlsx'

    for row in result:
        new_row = {
            'year': row[0],
            'month': row[1],
            'subtotal': row[2],
            'total_cost': row[3],
            'margin_amount': row[4],
            'margin_percent': row[5] 
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv(output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
    conn.close()

except pyodbc.Error as e:
    print(f"Error executing the SQL query: {e}")
    conn.close()
    exit()