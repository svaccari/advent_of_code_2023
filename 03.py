def is_near_symbol(x, y, w, h, data: list[str]):
    c = data[y][x]
    if not c.isdigit():
        return False
    for j in range(max(0, y - 1), min(h, y + 2)):
        for i in range(max(0, x - 1), min(w, x + 2)):
            c = data[j][i]
            if not c.isdigit() and c != ".":
                return True
    return False

def get_gear_coords(x, y, w, h, data: list[str]):
    c = data[y][x]
    if not c.isdigit():
        return None
    for j in range(max(0, y - 1), min(h, y + 2)):
        for i in range(max(0, x - 1), min(w, x + 2)):
            c = data[j][i]
            if not c.isdigit() and c == "*":
                return (j, i)
    return None

with open("03.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    w = len(lines[0])
    h = len(lines)

    numbers = []
    gears = {}
    for y in range(0, h):
        number = ""
        has_symbol = False
        gear_coord = None
        for x in range(0, w):
            if is_near_symbol(x, y, w, h, lines):
                has_symbol = True
            if get_gear_coords(x, y, w, h, lines):
                gear_coord = get_gear_coords(x, y, w, h, lines)
            c = lines[y][x]
            if c.isdigit():
                number += c
                continue
            if has_symbol and number:
                numbers.append(int(number))
                if gear_coord:
                    if gear_coord in gears:
                        gears[gear_coord].append(int(number))
                    else:
                        gears[gear_coord] = [int(number)]
            number = ""
            has_symbol = False
            gear_coord = None
        if has_symbol and number:
            numbers.append(int(number))
            if gear_coord:
                if gear_coord in gears:
                    gears[gear_coord].append(int(number))
                else:
                    gears[gear_coord] = [int(number)]

    # Part 1
    sum = sum(numbers)
    print("Sum part 1: ", sum)

    # Part 2
    sum = 0
    for numbers in gears.values():
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]

    print("Sum part 2: ", sum)
