import sys
import datetime

f = "%Y-%m-%d %H:%M:%S %Z%z"
d = datetime.datetime.strptime(sys.argv[1], f)
d = d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=int(sys.argv[2])))) + datetime.timedelta(hours=int(sys.argv[2]))
if len(sys.argv) > 4:
    dst_start = datetime.datetime.strptime(sys.argv[3], f)
    dst_end = datetime.datetime.strptime(sys.argv[4], f)
elif len(sys.argv) > 3:
    print('Warning: Not enough values present to use daylight saving time mode.', file=sys.stderr)

