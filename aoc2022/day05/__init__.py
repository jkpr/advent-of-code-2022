from collections import deque
from re import findall


def build_loading_bay(crate_string: str) -> list[deque[str]]:
    loading_bay = []
    lines = crate_string.split("\n")
    columns = list(zip(*lines))
    for column in columns:
        if column[-1].isdigit():
            stack = deque(filter(lambda x: x.isalpha(), column))
            loading_bay.append(stack)
    return loading_bay


def move_crate(loading_bay: list[deque[str]], origin: int, destination: int):
    origin_stack = loading_bay[origin]
    crate = origin_stack.popleft()
    destination_stack = loading_bay[destination]
    destination_stack.appendleft(crate)


def part1(lines: list[str]):
    chunks = "\n".join(lines).split("\n\n")
    crate_string = chunks[0]
    loading_bay = build_loading_bay(crate_string)
    instructions = chunks[1].split("\n")
    for instruction in instructions:
        quantity, origin, destination = [int(i) for i in findall(r"\d+", instruction)]
        for _ in range(quantity):
            move_crate(loading_bay, origin - 1, destination - 1)
    return "".join([s[0] for s in loading_bay])


def move_crate2(
    loading_bay: list[deque[str]], quantity: int, origin: int, destination: int
):
    crane = []
    origin_stack = loading_bay[origin]
    destination_stack = loading_bay[destination]
    for _ in range(quantity):
        crane.append(origin_stack.popleft())
    for _ in range(quantity):
        destination_stack.appendleft(crane.pop())


def part2(lines: list[str]):
    chunks = "\n".join(lines).split("\n\n")
    crate_string = chunks[0]
    loading_bay = build_loading_bay(crate_string)
    instructions = chunks[1].split("\n")
    for instruction in instructions:
        quantity, origin, destination = [int(i) for i in findall(r"\d+", instruction)]
        move_crate2(loading_bay, quantity, origin - 1, destination - 1)
    return "".join([s[0] for s in loading_bay])
