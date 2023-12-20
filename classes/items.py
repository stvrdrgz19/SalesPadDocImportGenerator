class Items:
    def __init__(self, number, type):
        self.number = number
        self.type = type

    def display_info(self):
        print(f"Number: {self.number}, Type: {self.type}")

    def get_item_list():
        ssd128 = Items("128 SSD", "Inventory")
        ssd256 = Items("256 SSD", "Inventory")
        ssd512 = Items("512 SSD", "Inventory")
        nvme128 = Items("128 NVME", "Inventory")
        nvme256 = Items("256 NVME", "Inventory")
        nvme512 = Items("512 NVME", "Inventory")
        dualcore = Items("DUAL-CORE", "Inventory")
        quadcore = Items("QUAD-CORE", "Inventory")
        eightcore = Items("EIGHT-CORE", "Inventory")
        hpoffice8710 = Items("HP-OFFICE-8710", "Inventory")
        hpoffice7740 = Items("HP-OFFICE-7740", "Inventory")
        hpoffice9015 = Items("HP-OFFICE-9015", "Inventory")
        hpdesk7740 = Items("HP-DESK-7740", "Inventory")
        hpdesk9019 = Items("HP-DESK-9019", "Inventory")
        hpdesk8600 = Items("HP-DESK-8600", "Inventory")
        dcgold600 = Items("DC-GOLD-600", "Inventory")
        dcgold700 = Items("DC-GOLD-700", "Inventory")
        dcgold800 = Items("DC-GOLD-800", "Inventory")
        dcsilver600 = Items("DC-SILVER-600", "Inventory")
        dcsilver700 = Items("DC-SILVER-700", "Inventory")
        dcsilver800 = Items("DC-SILVER-800", "Inventory")
        rtx3060 = Items("RTX-3060", "Inventory")
        rtx3070 = Items("RTX-3070", "Inventory")
        rtx4070 = Items("RTX-4070", "Inventory")
        sc1001 = Items("SC-1001", "Inventory")
        sc2002 = Items("SC-2002", "Inventory")
        sc3003 = Items("SC-3003", "Inventory")
        ah1001 = Items("AH-1001", "Inventory")
        ah2002 = Items("AH-2002", "Inventory")
        ah3003 = Items("AH-3003", "Inventory")
        cab1001 = Items("CAB-1001", "Inventory")
        cab2002 = Items("CAB-2002", "Inventory")
        cab3003 = Items("CAB-3003", "Inventory")
        desk1001 = Items("DESK-1001", "Inventory")
        desk2002 = Items("DESK-2002", "Inventory")
        desk3003 = Items("DESK-3003", "Inventory")
        chair1001 = Items("CHAIR-1001", "Inventory")
        chair2002 = Items("CHAIR-2002", "Inventory")
        chair3003 = Items("CHAIR-3003", "Inventory")
        supp1001 = Items("SUPP-1001", "Service")
        supp2002 = Items("SUPP-2002", "Service")
        supp3003 = Items("SUPP-3003", "Service")
        dcp1001 = Items("DCP-1001", "Kit")
        dcp2002 = Items("DCP-2002", "Kit")
        dcp3003 = Items("DCP-3003", "Kit")

        item_list = [
            ssd128,
            ssd256,
            ssd512,
            nvme128,
            nvme256,
            nvme512,
            dualcore,
            quadcore,
            eightcore,
            hpoffice8710,
            hpoffice7740,
            hpoffice9015,
            hpdesk7740,
            hpdesk9019,
            hpdesk8600,
            dcgold600,
            dcgold700,
            dcgold800,
            dcsilver600,
            dcsilver700,
            dcsilver800,
            rtx3060,
            rtx3070,
            rtx4070,
            sc1001,
            sc2002,
            sc3003,
            ah1001,
            ah2002,
            ah3003,
            cab1001,
            cab2002,
            cab3003,
            desk1001,
            desk2002,
            desk3003,
            chair1001,
            chair2002,
            chair3003,
            supp1001,
            supp2002,
            supp3003,
            dcp1001,
            dcp2002,
            dcp3003
        ]

        return item_list