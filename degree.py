
from collections import Counter
from re import split

BANNER = "-" * 35

def format_print(counter, is_reverse=False):
    lst = counter.items()
    lst.sort(key=lambda (a, b): (b, a), reverse=is_reverse)
    print ("[Unique Genes: %d]" % len(lst)).center(35, "=")
#    print "%-16s | %16s" % ("Genes", "Degree")
    print "%s\t%s" % ("Genes", "Degree")
    print BANNER
    for word, count in lst:
#        print "%-16s | %16d" % (word, count)
        print "%s\t%d" % (word, count)

def count_words(filename):
    counter = Counter()
    with open(filename, "rU") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
#            counter.update(x for x in split("[^a-zA-Z']+", line) if x)
            counter.update(x for x in split('\n', line) if x)
    return counter

format_print(count_words("words.txt"), is_reverse=False)
