from dataclasses import dataclass
from operator import attrgetter

class Game:
    winning: list[int] = []
    card: list[int] = []
    
    
with open("04.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    lines = [line.split(":")[1].strip() for line in lines]

    games = []

    for line in lines:
        tokens = line.split("|")
        game = Game()
        game.winning = [int(n) for n in tokens[0].split(" ") if n]
        game.card = [int(n) for n in tokens[1].split(" ") if n]
        games.append(game)

    # Part 1
    sum_part1 = 0
    for game in games:
        win = 0
        for c in game.card:
            if c in game.winning:
                win += 1
        if win:
            sum_part1 += 2**(win - 1)

    print("Sum: ", sum_part1) # 21558

    # Part 2
    count = {i:1 for i in range(0, len(lines))}
    for index, game in enumerate(games):
        for times in range(0, count[index]):
            win = 0
            for c in game.card:
                if c in game.winning:
                    win += 1
            if win:
                for next in range(index + 1, index + 1 + win):
                    count[next] += 1

    sum_part2 = sum(count.values())
    print("Sum: ", sum_part2) # 10425665
