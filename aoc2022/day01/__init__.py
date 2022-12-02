def part1(lines: list[str]):
    chunks = "\n".join(lines).split("\n\n")
    return max(sum(int(line) for line in chunk.split()) for chunk in chunks)


def part2(lines: list[str]):
    chunks = "\n".join(lines).split("\n\n")
    totals = sorted(sum(int(line) for line in chunk.split()) for chunk in chunks)
    return sum(totals[-3:])
