            # Task_11_1
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатый.

import calendar, datetime
year=2023
'''
begin=datetime.date(year, 1, 1)
fin=datetime.date(year, 12, 31)
date=begin
while date!=fin:
    if calendar.weekday(date.year, date.month, date.day) == 3 :
        print(date, ' - посещение Эрмитажа бесплатно')
    date=date+datetime.timedelta(days=1)
'''
# Работа над ошибками
mont=1
while mont!=13:
    de_1=calendar.monthrange(year, mont)
#    print(mont, de_1)
    if de_1[0]==3:
        free_day=15
    elif  de_1[0]>3:
        free_day=(6-de_1[0])+19
    elif de_1[0]<3:
        free_day=(3-de_1[0])+3+12
#    print('в ', mont, 'месяце ', 'посещение Эрмитажа бесплатно ', free_day, 'числа')
    print(datetime.date(year, mont, free_day), 'посещение Эрмитажа бесплатно ')
    mont+=1


