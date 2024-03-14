import pandas as pd

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
