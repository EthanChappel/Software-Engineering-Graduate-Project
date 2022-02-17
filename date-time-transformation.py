import sys
import datetime

f = "%Y-%m-%d %H:%M:%S %Z%z"
d = datetime.datetime.strptime(sys.argv[1], f)
d = d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=int(sys.argv[2])))) + datetime.timedelta(hours=int(sys.argv[2]))
print(d.strftime("%Y-%m-%d %H:%M:%S %Z"))