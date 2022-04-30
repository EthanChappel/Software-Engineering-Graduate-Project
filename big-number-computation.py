import sys

def to_int(s):
    try:
        return int(s)
    except ValueError:
        print('Error: \'%s\' is not an integer.' % s, file=sys.stderr)
        sys.exit(1)

if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*':
    print('Error: Operator must be \'+\' or \'-\'', file=sys.stderr)
    sys.exit(2)

a_s = None
b_s = None
d_s = None
if '.' in sys.argv[1] and '.' in sys.argv[3]:
    print('Error: Only one value can have a decimal.', file=sys.stderr)
    sys.exit(3)

elif ('.' in sys.argv[1] or '.' in sys.argv[3]) and sys.argv[2] == '*':
    print('Error: No value can have a decimal point if multiplying.')
    sys.exit(4)

if '.' in sys.argv[1]:
    a_s, d_s = sys.argv[1].split('.')
    b_s = sys.argv[3]
elif '.' in sys.argv[3]:
    a_s = sys.argv[1]
    b_s, d_s = sys.argv[3].split('.')
else:
    a_s = sys.argv[1]
    b_s = sys.argv[3]
    d_s = []

a_n = to_int(a_s)
b_n = to_int(b_s)
if len(d_s) > 0:
    d_n = to_int(d_s)
else:
    d_n = 0

if sys.argv[2] == '+':
    r = a_n + b_n
elif sys.argv[2] == '-':
    r = a_n - b_n
elif sys.argv[2] == '*':
    r = a_n * b_n

if sys.argv[2] == '-' and d_n > 0:
    z = int('1' + ('0' * (len(d_s))))
    d_n = z - d_n
    r += 1

if d_n > 0:
    print('%d.%d' % (r, d_n))
else:
    print(r)