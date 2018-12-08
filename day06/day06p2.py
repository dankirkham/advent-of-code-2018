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

def replace(before, after):
    for cell in np.ndindex(shape):
        x, y = cell

        if grid[x, y] == before:
            grid[x, y] = after

def output():
    s = ""
    for cell in np.ndindex(shape):
        x, y = cell
        if y == 0:
            s += '\n'

        s += str(grid[x, y])

    return s

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

grid = np.zeros(shape, dtype=int)

for cell in np.ndindex(shape):
    x, y = cell

    if grid[x, y] == 0:
        total_distance = sum(map(lambda c: manhattan_distance(c, (x + offset[0], y + offset[1])), coords))

        if total_distance < 10000:
            grid[x, y] = 1

def process_neighbors(cell, next_id):
    x, y = cell

    if grid[x, y] == 1:
        neighbors = set()

        if x > 0 and grid[x - 1, y] > 1:
            neighbors.add(grid[x - 1, y])

        if x < shape[0] - 2 and grid[x + 1, y] > 1:
            neighbors.add(grid[x + 1, y])

        if y > 0 and grid[x, y - 1] > 1:
            neighbors.add(grid[x, y - 1])

        if y < shape[1] - 2 and grid[x, y + 1] > 1:
            neighbors.add(grid[x, y + 1])

        if not neighbors:
            grid[x, y] = next_id
            next_id += 1
        elif len(neighbors) == 1:
            grid[x, y] = neighbors.pop()
        else:
            # Regions must be merged
            target = neighbors.pop()
            for region in neighbors:
                replace(region, target)

    return next_id

next_id = 2
for cell in np.ndindex(shape):
    next_id = process_neighbors(cell, next_id)

# I have to run this twice for some reason...
for cell in np.ndindex(shape):
    next_id = process_neighbors(cell, next_id)

print(Counter(np.ndarray.flatten(grid)))
