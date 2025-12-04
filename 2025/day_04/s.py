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
    dirs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
    ]
    res = []
    for row, row_line in enumerate(data):
        for col, elt in enumerate(row_line):
            if elt == "@":
                around = 0
                for d in dirs:
                    up = d[0]
                    right = d[1]
                    if (
                        row + up >= 0
                        and row + up < len(data)
                        and col + right < len(data[0])
                        and col + right >= 0
                    ):
                        if data[row + up][col + right] == "@":
                            around += 1
                if around < 4:
                    res.append((row, col))
    return res


def part1(data: list[list[str]]):
    return len(get_rolls_pos(data))


def part2(data: list[list[str]]):
    to_remove = get_rolls_pos(data)
    ans = 0
    while len(to_remove) > 0:
        for i, j in to_remove:
            data[i][j] = "."
        ans += len(to_remove)
        to_remove = get_rolls_pos(data)
    return ans


print(part1(data))
print(part2(data))
