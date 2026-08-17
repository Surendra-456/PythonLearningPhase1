import datetime
from datetime import timezone

# Current UTC date and time (timezone-aware)
now = datetime.datetime.now(tz=timezone.utc)
print("UTC Date and Time:", now)

# Current local date only
currentdate = datetime.date.today()
print("Current Date:", currentdate)

# Current UTC date and time (naive datetime)
dateutc = datetime.datetime.utcnow()
print("UTC Date and Time (naive):", dateutc)

# Current local date and time
local_now = datetime.datetime.now()
print("Local Date and Time:", local_now)

# # Current local date and time
# now = datetime.datetime.now()
# print("Local Date and Time:", now)

# # Current local date only
# currentdate = datetime.date.today()
# print("Current Date:", currentdate)

# # Current UTC date and time
# dateutc = datetime.datetime.utcnow()
# print("UTC Date and Time:", dateutc)