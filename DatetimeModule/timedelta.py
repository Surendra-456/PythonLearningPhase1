from datetime import datetime, timedelta


# 1 day, 2 hours, 30 minutes
delta = timedelta(days=1, hours=2, minutes=30)

print(delta)

#adding timedelta to current datetime
now = datetime.now()

future = now + timedelta(days=7)

print(now)
print(future)

#subtracting timedelta from current datetime
past = now - timedelta(hours=5)

print(past)

#subtracting two datetime objects to get a timedelta
start = datetime(1987, 12, 8, 7, 19, 0)
end = datetime(2026, 8, 17, 17, 30, 0)
delta = end - start

print(delta)
print(type(delta))
print(delta.days)
print(type(delta.days))
print(delta.seconds)
print(type(delta.seconds))