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

a = to_int(sys.argv[1])
b = to_int(sys.argv[3])
print(a + (b if sys.argv[2] == '+' else -b))