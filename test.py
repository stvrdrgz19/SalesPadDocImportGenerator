from utils import Trends, get_items_cost_price, DBType
from classes.dates import get_dates_with_trends
from datetime import datetime, timedelta
import pandas as pd
import random
import numpy as np

trend = random.choice([member.name for member in Trends])
dates = get_dates_with_trends("2022-01-01", "2024-03-13", trend, 40)
dates.sort()
print(dates)
print(len(dates))

# test = ["test", "test2"]
# print(type(test))
# my_float = 3.14159

# rounded_integer = round(my_float)

# print(rounded_integer)

# dates = get_dates_with_trends('2024-01-01', '2024-01-18', Trends.Increase.name, 1)
# dates.sort()

# date_format = "%Y-%m-%d"

# for date in dates:
#     # datetime_obj = datetime.utcfromtimestamp(date.tolist() / 1e9)
#     # print(datetime_obj.strftime(date_format))
#     # print(type(date))
#     datetime_date = date.astype(datetime)
#     print(date)

# items = get_items_cost_price(DBType.TWO, 'Each')
# for item in items:
#     print(item.number)

# start_range = 1.0
# end_range = 5.0
# random_float_range = (round(random.uniform(start_range, end_range), 1))*10

# factor = f'1.{random_float_range}'.rstrip(".0")

# # Display the result
# print(float(factor))

# data = {
#     'Col1': [1, 1, 1, 2, 2, 2, 3, 3],
#     'Col2': ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],
#     'Col3': [0, 0, 0, 0, 0, 0, 0, 0]
# }
# df = pd.DataFrame(data)

# df.loc[(df['Col1'] == 2) & (df['Col2'] == 'b'), 'Col3'] = 5

# print(df)

# date_range = ["2024-01-01", "2024-01-18"]

# start_date = datetime.strptime(date_range[0], '%Y-%m-%d')
# end_date = datetime.strptime(date_range[1], '%Y-%m-%d')
# days_difference = round(((end_date - start_date).days)/4)
# modify_from_date = end_date - timedelta(days=days_difference)
# np_date = np.datetime64(start_date)

# date_format = "%Y-%m-%d"

# for date in dates:
#     if date > np_date:
#         print("Greater")
#     else:
#         print("Lesser")

# names = [
#     'Malcom',
#     'Stuart',
#     'Sam',
#     'Phillip'
# ]

# data = {
#     'Date': ['2024-01-15T00:00:00.000000000', '2024-01-16T00:00:00.000000000', '2024-01-17T00:00:00.000000000', '2024-01-18T00:00:00.000000000'],
#     'Name': ['Jean', 'Malcom', 'Dwayne', 'Sam'],
#     'UnitPrice': ['11.12', '33.33', '14.02', '51.51']
# }
# df = pd.DataFrame(data)
