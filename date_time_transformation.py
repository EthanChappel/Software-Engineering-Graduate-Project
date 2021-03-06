import sys
import datetime


DT_FORMAT = '%Y-%m-%dT%H:%M:%S%z'


def transform_datetime(d, offset, dst_start = None, dst_end = None):
    old_is_utc = d.utcoffset().total_seconds() == 0
    d = d.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=offset))) \
        - d.utcoffset() \
        + datetime.timedelta(hours=offset)
    new_is_utc = d.utcoffset().total_seconds() == 0

    if dst_start is not None and dst_end is not None:
        if dst_start <= d and d < dst_end:
            if old_is_utc:
                d += datetime.timedelta(hours=1)
            if new_is_utc:
                d -= datetime.timedelta(hours=1)

    return d

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough arguments.", file=sys.stderr)
        sys.exit(1)

    d = datetime.datetime.strptime(sys.argv[1], DT_FORMAT)
    offset = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if len(sys.argv) == 4:
        print('Warning: Not enough arguments to use daylight saving time mode.', file=sys.stderr)

    if offset is not None:
        if offset < -12 or offset > +14:
            print('Error: Timezone must be within -12 and +14.', file=sys.stderr)
            sys.exit(2)

        d = transform_datetime(
            d,
            offset,
            datetime.datetime.strptime(sys.argv[3], DT_FORMAT) if len(sys.argv) > 4 else None,
            datetime.datetime.strptime(sys.argv[4], DT_FORMAT) if len(sys.argv) > 4 else None
        )

    print(d.strftime("%s %%A" % DT_FORMAT))
