class Line:
    def __init__(self, line_num, component_seq_num, item_num, quantity, quantity_bo, uofm, markdown_percent, price):
        self.line_num = line_num
        self.component_seq_num = component_seq_num
        self.item_num = item_num
        self.quantity = quantity
        self.quantity_bo = quantity_bo
        self.uofm = uofm
        self.markdown_percent = markdown_percent
        self.price = price