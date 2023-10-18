from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import random

def generate_unique_dates_in_range(start_date, end_date, days_per_month):
    unique_dates = []

    current_month = start_date.replace(day=1)
    
    while current_month <= end_date:
        last_day_of_month = current_month + relativedelta(day=31)
        
        if current_month == start_date:
            last_day_of_month = min(last_day_of_month, end_date)
            
            # Adjust the range for the first month
            days_range = (last_day_of_month - current_month).days + 1
        else:
            days_range = (last_day_of_month - current_month).days
        
        for _ in range(days_per_month):
            if days_range > 0:
                random_day = current_month + timedelta(days=random.randint(0, days_range))
                unique_dates.append(random_day)
        
        current_month += relativedelta(months=1)
    
    return unique_dates

# Example usage:
start_date = datetime(2022, 10, 18)  # Replace with your start date
end_date = datetime(2023, 10, 18)    # Replace with your end date
days_per_month = 2

unique_dates = generate_unique_dates_in_range(start_date, end_date, days_per_month)

for date in unique_dates:
    print(date.strftime("%Y-%m-%d"))