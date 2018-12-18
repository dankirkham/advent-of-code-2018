from collections import deque
from itertools import cycle
import re

def parse_input():
    f = open('input9.in', 'r')

    m = re.search('(\d+) players; last marble is worth (\d+) points', f.readline())

    player_count = int(m.group(1))
    last_marble = int(m.group(2))

    f.close()

    return player_count, last_marble

class GameOver(Exception):
    pass

class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0

    def add_marbles(self, marbles):
        for marble in marbles:
            self.score += marble

class Circle:
    def __init__(self, last_marble):
        self.marbles = iter(range(last_marble + 1))
        self.circle = deque()
        self.circle.append(next(self.marbles))
        self.current_marble = 0

    def insert_marble(self, marble):
        idx = (self.current_marble + 2) % len(self.circle)
        if idx == 0:
            self.circle.append(marble)
            self.current_marble = len(self.circle) - 1
        else:
            self.circle.insert(idx, marble)
            self.current_marble = idx

        # collections.deque inefficiently implements insert using rotates.
        # Let's go ahead and rotate so that we will more than likely use an
        # append the next time this method is called, avoiding the insert
        # method altogether. The following code rotates backwards exactly one
        # time, most of the time. This speeds things up significantly.
        target = len(self.circle) - 2
        self.circle.rotate(target - self.current_marble)
        self.current_marble = target

    def remove_marble(self):
        idx = (self.current_marble - 7) % len(self.circle)

        removed_marble = self.circle[idx]
        del self.circle[idx]

        self.current_marble = idx
        if self.current_marble >= len(self.circle):
            self.current_marble = 0

        return removed_marble

    def play(self):
        players_marbles = set()

        try:
            marble = next(self.marbles)
        except StopIteration:
            raise GameOver()

        if marble % 23 != 0:
            self.insert_marble(marble)
        else:
            players_marbles.add(marble)
            players_marbles.add(self.remove_marble())

        return players_marbles

def run_game(player_count, last_marble):
    circle = Circle(last_marble)

    players = []
    for id in range(player_count):
        players.append(Player(id + 1))

    players_iter = cycle(players)

    try:
        while True:
            player = next(players_iter)

            players_marbles = circle.play()

            player.add_marbles(players_marbles)
    except GameOver:
        winner = max(player.score for player in players)
        print(winner)

player_count, last_marble = parse_input()

run_game(player_count, last_marble)
run_game(player_count, last_marble * 100)
