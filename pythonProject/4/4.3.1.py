def mag(date):
    day, month, year = map(int, date.split('.'))
    return day * month == year % 100

date1 = '02.11.2022'
date2 = '15.03.2021'

print(mag(date1))
print(mag(date2))