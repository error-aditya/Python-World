from datetime import datetime, timedelta
def get_tuesdays_and_fridays(year, month):
    dates = []
    first_day = datetime(year, month, 1)
    day = first_day

    while day.month == month:
        if day.weekday() in [1, 4]:  # 1 is Tuesday, 4 is Friday
            dates.append(day.strftime('%Y-%m-%d'))
        day += timedelta(days=1)

    return dates


year = int(input('Enter the year -> '))
month = int(input('Enter the month -> '))
tuesdays_and_fridays = get_tuesdays_and_fridays(year, month)
print(tuesdays_and_fridays)
