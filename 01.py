def get_number(line: str) -> int:
    chars = list(line)
    digits = [c for c in chars if c >= "0" and c <= "9"]
    return int(digits[0] + digits[-1])


def get_number_part2(line: str) -> int:
    tokens = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        else:
            for n, token in enumerate(tokens):
                if line[i:].startswith(token):
                    digits.append(str(n + 1))
    return int(digits[0] + digits[-1])


with open("01.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    # Part 1
    sum = 0
    for line in lines:
        sum += get_number(line)

    print(f"Part one: {sum}")

    # Part 2
    sum = 0
    for line in lines:
        sum += get_number_part2(line)

    print(f"Part two: {sum}")  # 54992
