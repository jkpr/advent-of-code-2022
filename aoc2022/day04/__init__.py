from collections import (
    Counter,
    defaultdict,
    deque,
    namedtuple,
)
from dataclasses import dataclass
from functools import cache
from itertools import (
    chain,
    combinations,
    groupby,
    permutations,
    product,
    repeat,
)
from math import (
    prod,
    sqrt,
)
from re import (
    search,
    match,
    fullmatch,
    split,
    findall,
    sub,
)


def create_range_sets(line: str) -> tuple[set[int], set[int]]:
    nums = [int(i) for i in findall(r"\d+", line)]
    left = set(range(nums[0], nums[1] + 1))
    right = set(range(nums[2], nums[3] + 1))
    return left, right


def part1(lines: list[str]):
    total = 0
    for line in lines:
        left, right = create_range_sets(line)
        inter = left & right
        total += inter == left or inter == right
    return total


def part2(lines: list[str]):
    total = 0
    for line in lines:
        left, right = create_range_sets(line)
        inter = left & right
        total += bool(inter)
    return total
