from utils import Trends
from classes.dates import get_dates_with_trends
from datetime import datetime

dates = get_dates_with_trends('2022-01-01', '2022-01-20', Trends.Increase.name, 10)
dates.sort()

date_format = "%Y-%m-%d"

for date in dates:
    datetime_obj = datetime.utcfromtimestamp(date.tolist() / 1e9)
    print(datetime_obj.strftime(date_format))