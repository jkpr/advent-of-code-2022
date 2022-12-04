LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(lines: list[str]):
    total = 0
    for line in lines:
        length = len(line) // 2
        first = line[:length]
        second = line[length:]
        intersection = set(first) & set(second)
        if intersection:
            letter = list(intersection)[0]
            total += LETTERS.index(letter) + 1
    return total


def part2(lines: list[str]):
    total = 0
    for i in range(len(lines) // 3):
        a, b, c = lines[i * 3 : (i * 3 + 3)]
        inter = list(set(a) & set(b) & set(c))[0]
        if inter:
            letter = list(inter)[0]
            total += LETTERS.index(letter) + 1
    return total
