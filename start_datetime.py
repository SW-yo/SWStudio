import datetime
"""
day = datetime.date(1966, 1, 12)
print(day)
print(day.weekday())

kyou = datetime.date.today()
print(kyou)

print(day.today())

apollo_11 = datetime.datetime(1969, 7, 21, 5, 17 ,40)
print(apollo_11)

ima = datetime.datetime.now()
print(ima)
"""
"""
date_a = datetime.date(2008, 1, 1)
date_b = datetime.date(2009, 1, 1)
days_2008 = date_b - date_a
print(days_2008)
"""

today = datetime.date.today()
birthday = datetime.date(1966, 1, 12)
life = today - birthday
print(life)