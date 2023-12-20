class Customer:
    def __init__(self, number, trend, scenario):
        self.number = number
        self.trend = trend
        self.scenario = scenario

    def display_info(self):
        print(f"Number: {self.number}, Trend: {self.trend}, Scenario: {self.scenario}")

    def get_customer_list():
        networks0001 = Customer("NETWORKS0001", "Increase", "Invoice")
        # atmorere0001 = Customer("ATMORERE0001", "Decrease", "Invoice") # originally Invoice scenario
        # unifiedw0001 = Customer("UNIFIEDW0001", "UpDown", "Invoice")
        # adampark0001 = Customer("ADAMPARK0001", "DownUp", "Invoice")
        # midcityh0001 = Customer("MIDCITYH0001", "Wave", "Invoice")
        # westside0001 = Customer("WESTSIDE0001", "Seasonal", "Invoice")
        # greenway0001 = Customer("GREENWAY0001", "Churn", "Invoice")
        # margiest0001 = Customer("MARGIEST0001", "Increase", "Invoice")
        # northern0001 = Customer("NORTHERN0001", "Decrease", "Invoice")
        # blueyond0001 = Customer("BLUEYOND0001", "UpDown", "Invoice")
        # directma0001 = Customer("DIRECTMA0001", "DownUp", "Invoice")
        # lasermes0001 = Customer("LASERMES0001", "Wave", "Invoice")
        # northcol0001 = Customer("NORTHCOL0001", "Seasonal", "Invoice")
        # homefurn0001 = Customer("HOMEFURN0001", "Churn", "Invoice")
        # astorsui0001 = Customer("ASTORSUI0001", "Increase", "Invoice")
        # cellular0001 = Customer("CELLULAR0001", "Decrease", "Invoice")
        # aaronfit0001 = Customer("AARONFIT0001", "UpDown", "Invoice")
        # cohowine0001 = Customer("COHOWINE0001", "DownUp", "Invoice")
        # contosol0001 = Customer("CONTOSOL0001", "Wave", "Invoice")
        # franchis0001 = Customer("FRANCHIS0001", "Seasonal", "Invoice")

        customer_list = [
            networks0001,
            # atmorere0001,
            # unifiedw0001,
            # adampark0001,
            # midcityh0001,
            # westside0001,
            # greenway0001,
            # margiest0001,
            # northern0001,
            # blueyond0001,
            # directma0001,
            # lasermes0001,
            # northcol0001,
            # homefurn0001,
            # astorsui0001,
            # cellular0001,
            # aaronfit0001,
            # cohowine0001,
            # contosol0001,
            # franchis0001
        ]

        return customer_list