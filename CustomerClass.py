class Customer:
    def __init__(self, number, trend, scenario):
        self.number = number
        self.trend = trend
        self.scenario = scenario

    def display_info(self):
        print(f"Number: {self.number}, Trend: {self.trend}, Scenario: {self.scenario}")

    def get_customer_list():
        networks0001 = Customer("NETWORKS0001", "Increase", "Invoice")
        atmorere0001 = Customer("ATMORERE0001", "Decrease", "OrderInvoice")
        unifiedw0001 = Customer("UNIFIEDW0001", "UpDown", "OrderInvoicePartial")
        adampark0001 = Customer("ADAMPARK0001", "DownUp", "OrderInvoiceSplit")
        midcityh0001 = Customer("MIDCITYH0001", "Wave", "Invoice")
        westside0001 = Customer("WESTSIDE0001", "Seasonal", "OrderInvoice")
        greenway0001 = Customer("GREENWAY0001", "Churn", "OrderInvoicePartial")
        margiest0001 = Customer("MARGIEST0001", "Increase", "OrderInvoiceSplit")
        northern0001 = Customer("NORTHERN0001", "Decrease", "Invoice")
        blueyond0001 = Customer("BLUEYOND0001", "UpDown", "OrderInvoice")
        directma0001 = Customer("DIRECTMA0001", "DownUp", "OrderInvoicePartial")
        lasermes0001 = Customer("LASERMES0001", "Wave", "OrderInvoiceSplit")
        northcol0001 = Customer("NORTHCOL0001", "Seasonal", "Invoice")
        homefurn0001 = Customer("HOMEFURN0001", "Churn", "OrderInvoice")
        astorsui0001 = Customer("ASTORSUI0001", "Increase", "OrderInvoicePartial")
        cellular0001 = Customer("CELLULAR0001", "Decrease", "OrderInvoiceSplit")
        aaronfit0001 = Customer("AARONFIT0001", "UpDown", "Invoice")
        cohowine0001 = Customer("COHOWINE0001", "DownUp", "OrderInvoice")
        contosol0001 = Customer("CONTOSOL0001", "Wave", "OrderInvoicePartial")
        franchis0001 = Customer("FRANCHIS0001", "Seasonal", "OrderInvoiceSplit")

        customer_list = [
            networks0001,
            atmorere0001,
            unifiedw0001,
            adampark0001,
            midcityh0001,
            westside0001,
            greenway0001,
            margiest0001,
            northern0001,
            blueyond0001,
            directma0001,
            lasermes0001,
            northcol0001,
            homefurn0001,
            astorsui0001,
            cellular0001,
            aaronfit0001,
            cohowine0001,
            contosol0001,
            franchis0001
        ]

        return customer_list