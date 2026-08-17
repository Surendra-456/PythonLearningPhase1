import datetime
import datetime_pytz

dt_mtn = datetime.datetime.now(tz=datetime_pytz.timezone('US/Mountain'))

# print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime