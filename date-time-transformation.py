import sys
import datetime

if len(sys.argv) < 3:
    print("Error: Not enough arguments to perform time zone transformation.", file=sys.stderr)
    sys.exit(1)

if int(sys.argv[2]) < -12 or int(sys.argv[2]) > +14:
    print('Error: Timezone must be within -12 and +14')
    sys.exit(2)


f = '%Y-%m-%dT%H:%M:%S%z'
d = datetime.datetime.strptime(sys.argv[1], f)
old_is_utc = d.utcoffset().total_seconds() == 0
d = d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=int(sys.argv[2])))) - d.utcoffset() + datetime.timedelta(hours=int(sys.argv[2])) + d.utcoffset()
new_is_utc = d.utcoffset().total_seconds() == 0

if len(sys.argv) > 4:
    dst_start = datetime.datetime.strptime(sys.argv[3], f)
    dst_end = datetime.datetime.strptime(sys.argv[4], f)

    if dst_start < d and d < dst_end:
        if old_is_utc:
            d += datetime.timedelta(hours=1)
        if new_is_utc:
            d -= datetime.timedelta(hours=1)

elif len(sys.argv) > 3:
    print('Warning: Not enough arguments to use daylight saving time mode.', file=sys.stderr)

print(d.strftime(f))