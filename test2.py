import matplotlib.pyplot as plt
from collections import Counter
from classes.dates import get_dates_with_trends

def visualize_data(dates):
    # remove duplicate dates
    unique_dates = list(set(dates))
    # sort dates
    unique_dates.sort()

    # get count per date
    count_dict = Counter(dates)
    count_list = list(count_dict.values())

    fig, ax = plt.subplots()
    ax.plot(unique_dates, count_list, label='Date Trends')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Date Trends')
    ax.legend()

    plt.show()

start_date = "2021-10-10"
end_date = "2023-10-10"
trend_value = "DownUp"
date_count = 1000
dates = get_dates_with_trends(start_date, end_date, trend_value, date_count)
visualize_data(dates)
print('Complete...')