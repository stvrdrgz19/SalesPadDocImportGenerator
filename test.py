from utils import get_item_details, DBType
from classes.item_properties import ItemProperties

item_prop = get_item_details('256 SDRAM', 'Each', DBType.TWO)
print(item_prop.item_number)
