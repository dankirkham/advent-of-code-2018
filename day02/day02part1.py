from collections import Counter

f = open('input2.in', 'r')

twice = 0
thrice = 0

for line in f:
    characters = list(line)
    counts = Counter(characters)

    if 2 in counts.values():
        twice += 1

    if 3 in counts.values():
        thrice += 1
        
print(twice * thrice)
