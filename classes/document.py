class Document:
    def __init__(self, doc_num, doc_type, doc_id, customer_num, doc_date, warehouse, queue, freight, discount, lines) -> None:
        self.doc_num = doc_num
        self.doc_type = doc_type
        self.doc_id = doc_id
        self.customer_num = customer_num
        self.doc_date = doc_date
        self.warehouse = warehouse
        self.queue = queue
        self.freight = freight
        self.discount = discount
        self.lines = lines

    def sort_by_date(document):
        return document.doc_date