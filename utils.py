import random
import matplotlib.pyplot as plt
from collections import Counter

# randomly (within a threshold) determines if a document has freight/discount, as well as how much
def get_freight_or_discount(min_val, max_val, threshold, dec):
    percent = round(random.uniform(0, 100), 0)

    if percent < threshold:
        return 0
    
    else:
        return round(random.uniform(min_val, max_val), dec)

def visualize_data(dates, title):
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
    ax.set_title(title)
    ax.legend()

    plt.show()