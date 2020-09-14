import datetime
from datetime import timedelta

d = datetime.date(2013, 1, 1)
str_d = d.strftime('%m/%d/%Y')
print(str_d)
year, month, day = map(int, d.split('-'))
d = datetime.date(year, month, day)
print(d)
d = d.strftime('%m/%d/%Y')
d = datetime.date(d)+timedelta(days=30)
print(d)