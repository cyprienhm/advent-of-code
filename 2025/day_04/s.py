from itertools import product
from pathlib import Path

from utils import pad

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")
data = [[s for s in c] for c in data]
data = pad(data, 1, ".")


def get_rolls_pos(data: list[list[str]]):
    dirs = set(product([-1, 0, 1], [-1, 0, 1])) - {(0, 0)}
    res = []
    for row, row_line in enumerate(data):
        for col, elt in enumerate(row_line):
            if elt != "@":
                continue

            if (
                sum(data[row + up][col + right] == "@" for up, right in dirs)
                < 4
            ):
                res.append((row, col))
    return res


def get_rolls_pos_functional(data: list[list[str]]):
    dirs = set(product([-1, 0, 1], [-1, 0, 1])) - {(0, 0)}

    positions = list(product(range(len(data)), range(len(data[0]))))
    rolls = list(filter(lambda pos: data[pos[0]][pos[1]] == "@", positions))

    return list(
        filter(
            lambda rowcol: sum(
                data[rowcol[0] + up][rowcol[1] + right] == "@"
                for up, right in dirs
            )
            < 4,
            rolls,
        )
    )


def part1(data: list[list[str]]):
    return len(get_rolls_pos(data))


def part2(data: list[list[str]]):
    to_remove = get_rolls_pos_functional(data)
    ans = 0
    while len(to_remove) > 0:
        for i, j in to_remove:
            data[i][j] = "."
        ans += len(to_remove)
        to_remove = get_rolls_pos(data)
    return ans


print(part1(data))
print(part2(data))
