from collections import defaultdict
from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")

data = [
    [[int(elt) for elt in point.split(",")] for point in c.split(" -> ")]
    for c in data
]


def part1(data: list[list[list[int]]]):
    grid = defaultdict(int)

    for (p1x, p1y), (p2x, p2y) in data:
        if not (p1x == p2x or p1y == p2y):
            continue
        minx = min(p1x, p2x)
        maxx = max(p1x, p2x)
        miny = min(p1y, p2y)
        maxy = max(p1y, p2y)

        for xx in range(minx, maxx + 1):
            for yy in range(miny, maxy + 1):
                grid[(xx, yy)] += 1
    return len([c for c in grid if grid[c] >= 2])


def part2(data: list[list[list[int]]]):
    grid = defaultdict(int)

    for (p1x, p1y), (p2x, p2y) in data:
        minx = min(p1x, p2x)
        maxx = max(p1x, p2x)
        miny = min(p1y, p2y)
        maxy = max(p1y, p2y)
        if p1x == p2x or p1y == p2y:
            for xx in range(minx, maxx + 1):
                for yy in range(miny, maxy + 1):
                    grid[(xx, yy)] += 1
        else:
            dirx = 1 if p2x > p1x else -1
            diry = 1 if p2y > p1y else -1
            for ii in range(0, maxx - minx + 1):
                grid[(p1x + dirx * ii, p1y + diry * ii)] += 1

    return len([c for c in grid if grid[c] >= 2])


print(part1(data))
print(part2(data))
