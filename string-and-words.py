import sys
import string
import operator

word_count = {}

with open(sys.argv[1], 'r') as f:
    split = f.read().translate(str.maketrans('', '', string.punctuation)).split()
    for s in split:
        if s not in word_count.keys():
            word_count[s] = 1
        else:
            word_count[s] += 1

sorted_count = sorted(word_count.items(), reverse=True, key=operator.itemgetter(1))
for k in sorted_count:
    print("%s: %d" % (k[0], k[1]))