import random

games_to_play = 10000000

class Game(object):
    def __init__(self, strategy):
        self.money = 0
        self.strategy = strategy

    def run(self):
        if self.strategy.makeGuess() == random.randint(1, 6):
            self.money += 1
        else:
            self.money -= 1

class Always6(object):
    def makeGuess(self):
        return 6

class Always3(object):
    def makeGuess(self):
        return 3

class Random(object):
    def makeGuess(self):
        return random.randint(1, 6)

class Stair(object):
    def __init__(self):
        self.count = 0

    def makeGuess(self):
        self.count += 1
        return self.count % 5 + 1

if __name__ == '__main__':
    tosses = []
    for inst in (Always3(), Always6(), Random(), Stair()):
        g = Game(inst)
        for i in range(games_to_play):
            g.run()

        print ("%s\t %d " % (inst.__class__.__name__, g.money))