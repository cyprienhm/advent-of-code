from functools import reduce
from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def visible(row, col, data):
    w = len(data)
    h = len(data[0])
    beams = [
        data[row][col + 1 : w],
        data[row][0:col],
        [data[i][col] for i in range(row - 1, -1, -1)],
        [data[i][col] for i in range(row + 1, h)],
    ]
    return any(all(data[row][col] > c for c in beam) for beam in beams)


def part1(data: list[str]):
    data = [[int(i) for i in c] for c in data]

    return sum(
        visible(row, col, data)
        for row in range(len(data))
        for col in range(len(data[0]))
    )


def score(row, col, data):
    w = len(data)
    h = len(data[0])
    beams = [
        data[row][col + 1 : w],
        data[row][0:col][::-1],
        [data[i][col] for i in range(row - 1, -1, -1)],
        [data[i][col] for i in range(row + 1, h)],
    ]
    height = data[row][col]
    diffs = [[height - other for other in beam] for beam in beams]

    if any(len(diff) == 0 for diff in diffs):
        return 0

    views = []
    for diff in diffs:
        view = 0
        i = 0
        while i < len(diff) and diff[i] > 0:
            view += 1
            i += 1

        if i < len(diff):
            view += 1
        views.append(view)
    return reduce(lambda x, y: x * y, views, 1)


def part2(data: list[str]):
    data = [[int(i) for i in c] for c in data]

    return max(
        score(row, col, data)
        for row in range(len(data))
        for col in range(len(data[0]))
    )


print(part1(data))
print(part2(data))
