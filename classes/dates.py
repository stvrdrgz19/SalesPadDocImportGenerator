from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# get a trend based off of weight inputs
def trend(count, start_weight, end_weight):
    lin_sp = np.linspace(start_weight, end_weight, count)
    return lin_sp/sum(lin_sp)

# gets a number of dates between a range based off of a trend
def get_dates(start, end, doc_count, start_weight, end_weight):
    dates = pd.date_range(start, end, freq="D")
    date_trends = np.random.choice(dates, size=doc_count, p=trend(len(dates), start_weight, end_weight))
    return date_trends

# gets multiple sets of dates between ranges and trends
def get_dates_with_trends(start_date, end_date, trend, number_of_docs):
    #format dates
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)

    #get number of days within range
    days = end - start
    number_of_days = days.days

    if trend == "Increase":
        dates = get_dates(start_date, end_date, number_of_docs, 1, 15)
        return dates
    
    elif trend == "Decrease":
        dates = get_dates(start_date, end_date, number_of_docs, 15, 1)
        return dates

    if trend == "UpDown" or trend == "DownUp":
        days_per_direction = timedelta(days=round(number_of_days/2))
        docs_per_direction = round(number_of_docs/2)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + timedelta(days=1)
        dates1 = get_dates(start, first_end_day, round(docs_per_direction), 1, 15)
        dates2 = get_dates(second_start_day, end, round(docs_per_direction), 15, 1)
        return np.concatenate((dates1, dates2), axis=0)
    
    elif trend == "Wave":
        days_per_direction = timedelta(days=round(number_of_days/4))
        docs_per_direction = round(number_of_docs/4)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + timedelta(days=1)
        second_end_day = second_start_day + days_per_direction
        third_start_day = second_end_day + timedelta(days=1)
        third_end_day = third_start_day + days_per_direction
        fourth_start_day = third_end_day + timedelta(days=1)

        dates1 = get_dates(start, first_end_day, docs_per_direction, 1, 15)
        dates2 = get_dates(second_start_day, second_end_day, docs_per_direction, 15, 1)
        dates3 = get_dates(third_start_day, third_end_day, docs_per_direction, 1, 15)
        dates4 = get_dates(fourth_start_day, end, docs_per_direction, 15, 1)

        # concat dates in a weird way...
        dates_concat_1 = np.concatenate((dates1, dates2), axis=0)
        dates_concat_2 = np.concatenate((dates_concat_1, dates3), axis=0)
        return np.concatenate((dates_concat_2, dates4), axis=0)

    
    elif trend == "Seasonal":
        days_per_direction = timedelta(days=round(number_of_days/5))
        docs_per_direction = round(number_of_docs/3)

        first_end_day = start + days_per_direction
        second_start_day = first_end_day + days_per_direction
        second_end_day = second_start_day + days_per_direction
        third_start_day = second_end_day + days_per_direction

        dates1 = get_dates(start, first_end_day, docs_per_direction, 1, 15)
        dates2 = get_dates(second_start_day, second_end_day, docs_per_direction, 1, 15)
        dates3 = get_dates(third_start_day, end, docs_per_direction, 1, 15)

        # concat dates in a weird way...
        dates_concat_1 = np.concatenate((dates1, dates2), axis=0)
        return np.concatenate((dates_concat_1, dates3), axis=0)

    else:
        new_end_day = end - timedelta(days=370)
        new_days = new_end_day - start
        percent_of_days = new_days/days
        new_number_of_docs = round(number_of_docs * percent_of_days)

        dates = get_dates(start, new_end_day, new_number_of_docs, 15, 1)
        return dates