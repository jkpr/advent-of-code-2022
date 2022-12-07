def part1(lines: list[str]):
    line = lines[0]
    for i in range(len(line) - 4):
        end = i + 4
        chunk = line[i:end]
        if len(set(chunk)) == 4:
            return end


def part2(lines: list[str]):
    line = lines[0]
    for i in range(len(line) - 14):
        end = i + 14
        chunk = line[i:end]
        if len(set(chunk)) == 14:
            return end
