# from classes.dates import get_dates_with_trends

import utils

dates = utils.get_dates_with_trends('2022-01-01', '2022-01-20', 'Increase', 10)

for date in dates:
    print(date)