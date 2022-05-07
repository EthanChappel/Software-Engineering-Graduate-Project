import sys
import re
import string
import operator


def word_count(content):
    content = content.translate(str.maketrans('', '', string.punctuation)).split()
    word_count = {}

    for s in content:
        if s not in word_count.keys():
            word_count[s] = 1
        else:
            word_count[s] += 1

    return word_count



def word_replacement(old, new, content):
    return re.sub(r"\b%s\b" % old, new, content)


def grep_line(word, content):
    digits = len(str(len(content)))
    n = 0
    r = []

    for s in content.splitlines():
        n += 1
        if re.search(r"\b%s\b" % word, s):
            r.append("{n:{d}}:  {s}".format(n=n, d=digits, s=s.strip()))

    return r


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Not enough arguments.")
        sys.exit(4)
    elif sys.argv[1] == '-c':
        if len(sys.argv) < 3:
            print("Error: Not enough arguments to perform word count.", file=sys.stderr)
            sys.exit(1)

        try:
            with open(sys.argv[2], 'r') as f:
                split = f.read()
        except FileNotFoundError:
            print("Error: File %s not found." % sys.argv[2], file=sys.stderr)
            sys.exit(2)

        sorted_count = sorted(word_count(split).items(), reverse=True, key=operator.itemgetter(1))
        for k in sorted_count:
            print("%s: %d" % (k[0], k[1]))

    # word replacement
    elif sys.argv[1] == '-r':
        if len(sys.argv) < 6:
            print("Error: Not enough arguments to perform word replacment.", file=sys.stderr)
            sys.exit(3)

        try:
            with open(sys.argv[4], 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print("Error: File %s not found." % sys.argv[4], file=sys.stderr)
            sys.exit(2)

        replacement = word_replacement(sys.argv[2], sys.argv[3], content)

        with open(sys.argv[5], 'w') as f:
            f.write(replacement)

    # grepline
    elif sys.argv[1] == '-g':
        try:
            with open(sys.argv[3], 'r') as f:
                p = f.read()
        except FileNotFoundError:
            print("Error: File %s not found." % sys.argv[3], file=sys.stderr)
            sys.exit(2)
        except IndexError:
            print("Error: Not enough arguments to perform grepline.", file=sys.stderr)
            sys.exit(3)

        g = grep_line(sys.argv[2], p)
        for s in g:
            print(s)
