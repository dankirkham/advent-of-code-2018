import re
import numpy as np
from collections import Counter

def read_coords():
    coords = []

    with open('input06.in', 'r') as f:
        for line in f:
            m = re.search('(\d+), (\d+)', line)
            coords.append((int(m.group(1)), int(m.group(2))))

    return coords

def manhattan_distance(a, b):
    ax, ay = a
    bx, by = b

    return abs(by - ay) + abs(bx - ax)

coords = read_coords()

# Determine map size
x_coords, y_coords = zip(*coords)
shape = (
    max(x_coords) - min(x_coords),
    max(y_coords) - min(y_coords)
)
offset = (
    min(x_coords),
    min(y_coords)
)

map = np.zeros(shape, dtype=int)

for cell in np.ndindex(shape):
    x, y = cell

    closest = None
    for idx, coord in enumerate(coords):
        dis = manhattan_distance(coord, (x + offset[0], y + offset[1]))

        if not closest or closest['distance'] > dis:
            closest = {
                "index": idx + 1,
                "distance": dis
            }
        elif closest['distance'] == dis:
            closest = {
                "index": -1,
                "distance": dis
            }

    map[x, y] = closest['index']

infinite = set()
for x in range(shape[0]):
    infinite.add(map[x, 0])
    infinite.add(map[x, shape[1] - 1])

for y in range(shape[1]):
    infinite.add(map[0, y])
    infinite.add(map[shape[0] - 1, y])

counts = Counter(np.ndarray.flatten(map))

max_finite = 0
for key, val in counts.items():
    if key not in infinite:
        if val > max_finite:
            max_finite = val

print(max_finite)
