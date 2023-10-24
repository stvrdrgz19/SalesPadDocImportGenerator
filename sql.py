import pandas as pd
import pyodbc
import csv

server = 'sp-exporter-02\jayfluegel'
database = 'TWO'
username = 'sa'
password = 'sa'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print(f"Error connection to the database {e}")
    exit()

sql_query = """
SQL SCRIPT
"""

try:
    cursor = conn.cursor()
    cursor.execute(sql_query)

    result = cursor.fetchall()

    output_file = 'output\SQLResults.xslx'

    df = pd.DataFrame(result, columns=[column[0] for column in cursor.description])
    df.to_csv(output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)

    # for row in result:
        # print(row)

    conn.close()

except pyodbc.Error as e:
    print(f"Error executing the SQL query: {e}")
    conn.close()
    exit()