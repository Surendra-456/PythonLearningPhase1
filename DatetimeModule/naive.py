from datetime import datetime

dt = datetime.now()
print(dt)
print(dt.tzinfo)  # None

# Naive datetime: tzinfo=None (no timezone information).
# Aware datetime: tzinfo is set and represents an exact moment in time.
# Avoid mixing naive and aware datetimes in comparisons.
# Prefer UTC-aware datetimes (datetime.now(timezone.utc)) for storage and APIs.