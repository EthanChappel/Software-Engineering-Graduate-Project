import sys
import datetime


f = '%Y-%m-%dT%H:%M:%S%z'


def transform_datetime(d, offset, dst_start = None, dst_end = None):
    old_is_utc = d.utcoffset().total_seconds() == 0
    d = d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=offset))) - d.utcoffset() + datetime.timedelta(hours=offset)
    new_is_utc = d.utcoffset().total_seconds() == 0
    
    if dst_start != None and dst_end != None:
        if dst_start <= d and d < dst_end:
            if old_is_utc:
                d += datetime.timedelta(hours=1)
            if new_is_utc:
                d -= datetime.timedelta(hours=1)
    
    return d

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error: Not enough arguments to perform time zone transformation.", file=sys.stderr)
        sys.exit(1)

    if int(sys.argv[2]) < -12 or int(sys.argv[2]) > +14:
        print('Error: Timezone must be within -12 and +14')
        sys.exit(2)

    elif len(sys.argv) > 5:
        print('Warning: Not enough arguments to use daylight saving time mode.', file=sys.stderr)

    d = transform_datetime(
        datetime.datetime.strptime(sys.argv[1], f),
        int(sys.argv[2]),
        datetime.datetime.strptime(sys.argv[3], f) if len(sys.argv) > 4 else None,
        datetime.datetime.strptime(sys.argv[4], f) if len(sys.argv) > 4 else None
    )

    print(d.strftime("%s %%A" % f))