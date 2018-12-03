import numpy as np
import re

fabric = np.zeros((1000, 1000))

claims = list(open('input3.in', 'r'))

##1 @ 483,830: 24x18

for claim in claims:
    m = re.search('\#\d+ \@ (\d+)\,(\d+)\: (\d+)x(\d+)', claim)

    x, y, width, height = list(map(int, m.groups()))

    for i in range(x - 1, x + width - 1):
        for j in range(y - 1, y + height - 1):
            fabric[i, j] += 1

squares_with_two_or_more_claims = 0
for _, square in np.ndenumerate(fabric):
    if square > 1:
        squares_with_two_or_more_claims += 1

print(squares_with_two_or_more_claims)

for claim in claims:
    m = re.search('\#(\d+) \@ (\d+)\,(\d+)\: (\d+)x(\d+)', claim)

    id, x, y, width, height = list(map(int, m.groups()))

    overlapping = False
    for i in range(x - 1, x + width - 1):
        for j in range(y - 1, y + height - 1):
            if fabric[i, j] != 1:
                overlapping = True

    if not overlapping:
        print(id)
        break
