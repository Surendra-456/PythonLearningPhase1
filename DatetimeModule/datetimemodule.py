import datetime

manualDate=datetime.date(2023, 6, 1)
print(manualDate)
currentdate=datetime.date.today()
print(currentdate)
print(currentdate.weekday()) #sunday=6, monday=0, tuesday=1, wednesday=2, thursday=3, friday=4, saturday=5
print(currentdate.isoweekday()) #sunday=7, monday=1, tuesday=2, wednesday=3, thursday=4, friday=5, saturday=6
currentdatewithtime=datetime.datetime.now()
print(currentdatewithtime)