import re

acc = 0
freqs = set([acc])
first = False

def read_file(acc, freqs, first):
    f = open('input1.in', 'r')

    for line in f:
        m = re.search('([+-])(\d+)', line)

        val = int(m.group(2))

        if m.group(1) == '-':
            val = -val

        acc += val

        if not first:
            if acc in freqs:
                print("First frequency device reaches twice: {}".format(acc))
                first = True
            else:
                freqs.add(acc)

    f.close()

    return acc, freqs, first

acc, freqs, first = read_file(acc, freqs, first)
print("Final frequency: {}".format(acc))

# Keep running
while not first:
    acc, freqs, first = read_file(acc, freqs, first)
