import enum
from pathlib import Path

example = Path(__file__).parent / "example.txt"
example2 = Path(__file__).parent / "example2.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def join_back(cur: tuple[int, int], prev: tuple[int, int]) -> tuple[int, int]:
    curx, cury = cur
    prevx, prevy = prev
    if abs(cury - prevy) > 1:
        cury += 1 if cury < prevy else 0 if cury == prevy else -1
        curx += 1 if curx < prevx else 0 if curx == prevx else -1
    if abs(curx - prevx) > 1:
        curx += 1 if curx < prevx else 0 if curx == prevx else -1
        cury += 1 if cury < prevy else 0 if cury == prevy else -1
    return (curx, cury)


def part1(data: list[str]):
    instructions: list[tuple[str, int]] = [(c[0], int(c[2:])) for c in data]
    snake: list[tuple[int, int]] = [(0, 0) for _ in range(2)]

    pos_visited: set[tuple[int, int]] = set()

    head_updates = {
        "R": lambda head: (head[0] + 1, head[1]),
        "L": lambda head: (head[0] - 1, head[1]),
        "U": lambda head: (head[0], head[1] + 1),
        "D": lambda head: (head[0], head[1] - 1),
    }
    for direction, amount in instructions:
        for _ in range(amount):
            snake[0] = head_updates[direction](snake[0])

            for i in range(1, len(snake)):
                snake[i] = join_back(snake[i], snake[i - 1])
            pos_visited.add(snake[-1])
    return len(pos_visited)


def part2(data: list[str]):
    instructions: list[tuple[str, int]] = [(c[0], int(c[2:])) for c in data]
    snake: list[tuple[int, int]] = [(0, 0) for _ in range(10)]

    pos_visited: set[tuple[int, int]] = set()

    head_updates = {
        "R": lambda head: (head[0] + 1, head[1]),
        "L": lambda head: (head[0] - 1, head[1]),
        "U": lambda head: (head[0], head[1] + 1),
        "D": lambda head: (head[0], head[1] - 1),
    }
    for direction, amount in instructions:
        for _ in range(amount):
            snake[0] = head_updates[direction](snake[0])

            for i in range(1, len(snake)):
                snake[i] = join_back(snake[i], snake[i - 1])
            pos_visited.add(snake[-1])
    return len(pos_visited)


def print_snake(snake: list[tuple[int, int]]):
    print(snake)
    to_print = [["." for _ in range(-25, 25)] for _ in range(-10, 10)]
    for i, (x, y) in enumerate(snake):
        to_print[-y + 10][x + 25] = str(i)
    print("==")
    print("\n".join(["".join(c) for c in to_print]))
    print("==")


print(part1(data))
print(part2(data))
