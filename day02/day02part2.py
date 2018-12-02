from collections import Counter
import sys

with open('input2.in', 'r') as f:
    boxes = list(f)

boxes = list(map(lambda l: l.rstrip(), boxes))

def compare(a, b):
    differences = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1

            if differences > 1:
                return False

    if differences == 1:
        return True
    else:
        return False

def print_similar(a, b):
    for i in range(len(a)):
        if a[i] == b[i]:
            sys.stdout.write(a[i])

    sys.stdout.write('\n')

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        if compare(boxes[i], boxes[j]):
            print_similar(boxes[i], boxes[j])
