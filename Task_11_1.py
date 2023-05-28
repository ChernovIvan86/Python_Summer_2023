            # Task_11_1
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатый.

import calendar, datetime
year=2023
begin=datetime.date(year, 1, 1)
fin=datetime.date(year, 12, 31)
date=begin
while date!=fin:
    if calendar.weekday(date.year, date.month, date.day)==3:
        print(date, ' - посещение Эрмитажа бесплатно')
        if date <= begin + datetime.timedelta(days=9):
            print('но пока лучше не ходить')
    date=date+datetime.timedelta(days=1)



