from datetime import datetime, timezone
from zoneinfo import ZoneInfo

dt = datetime.now(timezone.utc)
dtlocal = dt.astimezone(ZoneInfo("Asia/Kathmandu"))

print(dt)
print(dt.tzinfo)

print(dtlocal)
print(dtlocal.tzinfo)

# datetime.now(timezone.utc)
# Creates an aware datetime in UTC.

# astimezone(ZoneInfo("Asia/Kathmandu"))
# Converts the same point in time to Kathmandu timezone.

# dt and dtlocal represent the same moment,
# but displayed in different timezones.