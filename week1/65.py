import datetime as dt
import time as tm

print dt
print tm

print tm.time()

#dtnow must be set as a variable
dtnow = dt.datetime.fromtimestamp(tm.time())
print dtnow


# see also following handy datetime attributes

print dtnow.year
print dtnow.month
print dtnow.day
print dtnow.hour,
print dtnow.minute, 
print dtnow.second

delta = dt.timedelta(days = 100)
print delta

today = dt.date.today()
print today - delta # the date 100 days ago
print today > today-delta #compare two dates

print today
