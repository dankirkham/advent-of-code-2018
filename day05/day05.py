from collections import deque
from tqdm import tqdm

with open('input05.in', 'r') as f:
    polymer = f.read()

polymer = deque(polymer)
polymer.pop() # Remove \n

def react(polymer):
    while True:
        reacted = False

        i = len(polymer) - 2
        while i >= 0:
            if polymer[i].lower() == polymer[i + 1].lower() and polymer[i].islower() ^ polymer[i + 1].islower():
                reacted = True
                del polymer[i + 1]
                del polymer[i]
                i -= 2
            else:
                i -= 1

        if not reacted:
            break

    return(len(polymer))

def remove(polymer, letter):
    new_polymer = polymer.copy()

    for i in reversed(range(len(new_polymer))):
        if new_polymer[i].lower() == letter.lower():
            del new_polymer[i]

    return new_polymer

print(react(polymer.copy()))

letters = 'abcdefghijklmnopqrstuvwxyz'
min_chain = None
min_letter = None
for letter in tqdm(letters):
    p = remove(polymer, letter)
    l = react(p)
    if not min_chain or l < min_chain:
        min_chain = l
        min_letter = letter
        
print(min_letter)
print(min_chain)
