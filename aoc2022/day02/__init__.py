GESTURE_MAP = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

SCORE_MAP = {
    0: 1,
    1: 2,
    2: 3,
}


def calculate_score(elf: str, me: str) -> int:
    diff = (GESTURE_MAP[me] - GESTURE_MAP[elf]) % 3
    if diff == 0:
        return 3 + SCORE_MAP[GESTURE_MAP[me]]
    elif diff == 1:
        return 6 + SCORE_MAP[GESTURE_MAP[me]]
    else:  # diff == 2:
        return 0 + SCORE_MAP[GESTURE_MAP[me]]


def part1(lines: list[str]):
    score = 0
    for line in lines:
        score += calculate_score(*line.split())
    return score


def calculate_score2(elf: str, outcome: str) -> int:
    if outcome == "X":
        return 0 + SCORE_MAP[(GESTURE_MAP[elf] + 2) % 3]
    elif outcome == "Y":
        return 3 + SCORE_MAP[GESTURE_MAP[elf]]
    else:  # outcome == "Z":
        return 6 + SCORE_MAP[(GESTURE_MAP[elf] + 1) % 3]


def part2(lines: list[str]):
    score = 0
    for line in lines:
        score += calculate_score2(*line.split())
    return score
