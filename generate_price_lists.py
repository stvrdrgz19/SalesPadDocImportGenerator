import pandas as pd
from utils import DBType, unit_of_measures, get_items_with_details, get_price_levels

db_type = DBType.TWO

items = get_items_with_details(db_type=db_type)
price_levels = get_price_levels(db_type=db_type)
file_path = "output/price_levels.xlsx"

df = pd.DataFrame(columns=[
    'ItemNumber',
    'CurrencyID',
    'PriceLevel',
    'UofM',
    'FromQty',
    'ToQty',
    'UofMPrice'
])

for item in items:
    for price_level in price_levels:
        for uofm in unit_of_measures:
            if uofm == 'Each':
                uofm_price = item.each_price
            else:
                uofm_price = item.case_price
            new_row = {
                'ItemNumber': item.item_number,
                'CurrencyID': 'Z-US$',
                'PriceLevel': price_level,
                'UofM': uofm,
                'FromQty': 1,
                'ToQty': 999999999999,
                'UofMPrice': uofm_price
            }
            
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df.to_excel(file_path, index=False, sheet_name="Sheet1")
print(f"Document generated at '{file_path}'")