import sys

def to_int(s):
    try:
        return int(s)
    except ValueError:
        print('Error: \'%s\' is not an integer.' % s)
        sys.exit(1)

if sys.argv[2] != '+' and sys.argv[2] != '-':
    print('Error: Operator must be \'+\' or \'-\'')
    sys.exit(2)

a_s = None
b_s = None
d_s = None
if '.' in sys.argv[1] and '.' in sys.argv[3]:
    print('Error: Only one value can have a decimal.')
    sys.exit(3)
if '.' in sys.argv[1]:
    a_s, d_s = sys.argv[1].split('.')
    b_s = sys.argv[3]
elif '.' in sys.argv[3]:
    a_s = sys.argv[1]
    b_s, d_s = sys.argv[3].split('.')

a_n = to_int(a_s)
b_n = to_int(b_s)
d_n = to_int(d_s)

r = a_n + (b_n if sys.argv[2] == '+' else -b_n)

if sys.argv[2] == '-' and d_n > 0:
    z = int('1' + ('0' * (len(d_s))))
    d_n = z - d_n
    r += 1

print("%d.%d" % (r, d_n))