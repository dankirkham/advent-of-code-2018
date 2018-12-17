import re
from collections import defaultdict

# Step G must be finished before step I can begin.

def build_dicts():
    parents = defaultdict(set)
    children = defaultdict(set)
    nodes = set()
    with open('input7.in') as f:
        for line in f:
            m = re.search('Step (\w) must be finished before step (\w) can begin\.', line)
            if m:
                child = m.group(1)
                parent = m.group(2)

                children[parent].add(child)
                parents[child].add(parent)

                nodes.add(child)
                nodes.add(parent)

    return nodes, parents, children

def find_roots(nodes, children):
    """Find child with no parents, i.e. the root of the tree."""
    roots = set()

    for node in nodes:
        if not children[node]:
            roots.add(node)

    return roots

def traverse(availiable_steps, parents, children, steps=None):
    """Recursively traverse tree to build sequence string."""
    if not steps:
        steps = set()

    # Take next step, if possible
    try:
        next_step = next(iter(sorted(list(availiable_steps))))
        availiable_steps.remove(next_step)
        steps.add(next_step)
    except StopIteration:
        return ''

    # Add parents of step taken
    for parent in parents[next_step]:
        if parent not in steps and children[parent].issubset(steps):
            availiable_steps.add(parent)

    # Recursive call
    return next_step + traverse(availiable_steps, parents, children, steps=steps)

nodes, parents, children = build_dicts()

roots = find_roots(nodes, children)

print(traverse(roots, parents, children))
