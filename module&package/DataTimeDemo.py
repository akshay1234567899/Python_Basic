import datetime
from time import timezone

from numpy.ma.core import subtract

# class-1 : datetime.date (working with dates)
# class-2 :datetime.time (working with time)
# class-3 : datetime.datetime (combination of both)
# class-4 : datetime.timedelta (representation of the duration )
# class-5 : datetime.tzinfo (base class or deleing with zone)

# current date and time :
current_datetime=datetime.datetime.now()
print("the current date and time", current_datetime)


current_date=datetime.date.today()
print("the current date",current_date)

now = datetime.datetime.now()
print("the current year",current_datetime.year)
print("the second",now.second)

# date arithematic with time delta ()
# add and subtract days

today=datetime.date.today()
future_date=today+datetime.timedelta(days=10)
print("10 days before today :",future_date)


from datetime import datetime, timezone
current_datetime = datetime.now(timezone.utc)

print("The current datetime with timezone:", current_datetime)

# ruchika@bebotechnologies.com
