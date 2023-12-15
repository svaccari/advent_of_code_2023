from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Hand:
    r: int = 0
    g: int = 0
    b: int = 0

with open("02.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    lines = [line.replace("Game ", "") for line in lines]

    games = {}
    for line in lines:
        tokens = line.split(":")
        game_number = int(tokens[0])

        hands = tokens[1].strip().split(";")
        game = []
        for hand_string in hands:
            hand = Hand()
            for color in hand_string.split(","):
                if "red" in color:
                    hand.r = int(color.strip().split(" ")[0])
                if "green" in color:
                    hand.g = int(color.strip().split(" ")[0])
                if "blue" in color:
                    hand.b = int(color.strip().split(" ")[0])
            game.append(hand)

        games[game_number] = game

    # Part 1
    # Max: 12 red cubes, 13 green cubes, and 14 blue cubes?
    r_max = 12
    g_max = 13
    b_max = 14

    sum = 0
    for id, game in games.items():
        if all(hand.r <= r_max and hand.g <= g_max and hand.b <= b_max for hand in game):
            sum += id

    print("Sum: ", sum)

    # Part 2
    sum = 0
    for game in games.values():
        r_min = max(game, key=attrgetter("r")).r
        g_min = max(game, key=attrgetter("g")).g
        b_min = max(game, key=attrgetter("b")).b
        sum += r_min * g_min * b_min

    print("Sum: ", sum)
