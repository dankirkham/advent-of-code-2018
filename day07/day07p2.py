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

class Worker:
    def __init__(self):
        self.timer = 0
        self.letter = None
        self._last_letter = None

    @property
    def busy(self):
        return self.timer > 0

    @property
    def last_letter(self):
        val = self._last_letter

        self._last_letter = None

        return val

    def do(self, letter):
        if not self.busy:
            self.timer = ord(letter) - 4
            # self.timer = ord(letter) - 4 - 60
            self.letter = letter
        else:
            raise RuntimeError("Can't let you do that, Star Fox")

    def tick(self):
        if self.busy:
            self.timer -= 1

            if self.timer == 0:
                self._last_letter = self.letter

def time_instructions(nodes, children, worker_count=5):
    # Create workers
    workers = []
    for _ in range(worker_count):
        workers.append(Worker())

    time = -1
    workers_busy = True

    letters = {
        "unprocessed": nodes,
        "waiting": set(),
        "done": set()
    }

    while workers_busy:
        # Tick workers
        for worker in workers:
            worker.tick()

        time += 1

        # Check old work
        if letters["waiting"]:
            for worker in workers:
                if not worker.busy:
                    completed_letter = worker.last_letter
                    if completed_letter:
                        letters["waiting"].remove(completed_letter)
                        letters["done"].add(completed_letter)

        # Allocate new work
        if letters["unprocessed"]:
            for worker in workers:
                if not worker.busy:
                    for unprocessed in list(sorted(letters["unprocessed"])):
                        deps = children[unprocessed]
                        if deps.issubset(letters["done"]):
                            worker.do(unprocessed)
                            letters["unprocessed"].remove(unprocessed)
                            letters["waiting"].add(unprocessed)
                            break

        # Check done status
        if len(letters["unprocessed"]) == 0 and len(letters["waiting"]) == 0:
            all_done = True
            for worker in workers:
                if worker.busy:
                    all_done = False

            if all_done:
                return time


nodes, parents, children = build_dicts()

roots = find_roots(nodes, children)

print(time_instructions(nodes, children))
