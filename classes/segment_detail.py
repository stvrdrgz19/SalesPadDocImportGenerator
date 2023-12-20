class SegmentDetail:
    def __init__(self, name, sales_amount_sum, gross_margin_sum, gross_margin_pct):
        self.name = name
        self.sales_amount_sum = sales_amount_sum
        self.gross_margin_sum = gross_margin_sum
        self.gross_margin_pct = gross_margin_pct

    def get_sales_amount(self):
        return self.sales_amount_sum
    
    def get_gross_margin(self):
        return self.gross_margin_sum
    
    def print_segment(self):
        print(f"Name: {self.name}")
        print(f"Sales Amount $: {self.sales_amount_sum}")
        print(f"Gross Margin $: {self.gross_margin_sum}")
        print(f"Gross Margin %: {self.gross_margin_pct}")
        print('')