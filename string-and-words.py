import sys
import re
import string
import operator

word_count = {}

if sys.argv[1] == '-c':
    if len(sys.argv) < 3:
        print("Error: Not enough arguments to perform word count.", file=sys.stderr)
        sys.exit(1)
    
    with open(sys.argv[2], 'r') as f:
        split = f.read().translate(str.maketrans('', '', string.punctuation)).split()
    
    for s in split:
        if len(sys.argv) > 4:
            if s == sys.argv[3]:
                s = sys.argv[4]
        if s not in word_count.keys():
            word_count[s] = 1
        else:
            word_count[s] += 1

    sorted_count = sorted(word_count.items(), reverse=True, key=operator.itemgetter(1))
    for k in sorted_count:
        print("%s: %d" % (k[0], k[1]))
elif sys.argv[1] == '-r':
    if len(sys.argv) < 6:
        print("Error: Not enough arguments to perform word replacment.", file=sys.stderr)
        sys.exit(2)
    
    with open(sys.argv[2], 'r') as f:
        contents = f.read()
    
    with open(sys.argv[3], 'w') as w:
        w.write(re.sub(r"\b%s\b" % sys.argv[4], sys.argv[5], contents))
