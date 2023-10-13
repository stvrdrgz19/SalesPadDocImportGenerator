import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

def trend(count, start_weight, end_weight):
    lin_sp = np.linspace(start_weight, end_weight, count)
    return lin_sp/sum(lin_sp)

# gets a number of dates between a range based off of a trend
def get_dates(start, end, doc_count, start_weight, end_weight):
    dates = pd.date_range(start, end, freq="B")
    date_trends = np.random.choice(dates, size=doc_count, p=trend(len(dates), start_weight, end_weight))
    return date_trends

dates = get_dates("2021-10-10", "2021-10-20", 30, 1, 15)
# dates.sort()
sorted_indices = np.argsort(dates)

sorted_dates = [dates[i] for i in sorted_indices]


unique_dates_list = list(set(sorted_dates))

count_dict = Counter(dates)
count_list = list(count_dict.values())

for item in count_list:
    print(item)

for date in unique_dates_list:
    print(date)

fig, ax = plt.subplots()

ax.plot(unique_dates_list, count_list, label='Trends')

ax.set_xlabel('Dates')
ax.set_ylabel('Count')
ax.set_title('Trends for dates')

ax.legend()

plt.show()
