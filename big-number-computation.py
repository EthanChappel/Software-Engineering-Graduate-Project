import sys


def to_int(s):
    try:
        return int(s)
    except ValueError:
        print('Error: \'%s\' is not an integer.' % s, file=sys.stderr)
        sys.exit(1)


def big_number_computation(a, o, b):
    a_s = None
    b_s = None
    d_s = None

    if '.' in a:
        a_s, d_s = a.split('.')
        b_s = b
    elif '.' in sys.argv[3]:
        a_s = a
        b_s, d_s = b.split('.')
    else:
        a_s = a
        b_s = b
        d_s = []

    a_n = to_int(a_s)
    b_n = to_int(b_s)
    if len(d_s) > 0:
        d_n = to_int(d_s)
    else:
        d_n = 0

    if o == '+':
        r = a_n + b_n
    elif o == '-':
        r = a_n - b_n
    elif o == '*':
        r = a_n * b_n

    if o == '-' and d_n > 0:
        z = int('1' + ('0' * (len(d_s))))
        d_n = z - d_n
        r += 1

    if d_n > 0:
        return '%d.%d' % (r, d_n)
    else:
        return str(r)


if __name__ == '__main__':
    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*':
        print('Error: Operator must be \'+\' or \'-\'', file=sys.stderr)
        sys.exit(2)

    if '.' in sys.argv[1] and '.' in sys.argv[3]:
        print('Error: Only one value can have a decimal.', file=sys.stderr)
        sys.exit(3)

    elif ('.' in sys.argv[1] or '.' in sys.argv[3]) and sys.argv[2] == '*':
        print('Error: No value can have a decimal point if multiplying.')
        sys.exit(4)

    print(big_number_computation(sys.argv[1], sys.argv[2], sys.argv[3]))