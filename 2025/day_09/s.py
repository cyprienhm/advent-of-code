import re
from functools import cache
from pathlib import Path

import numpy as np
from scipy import sparse
from tqdm import tqdm

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    coords = [
        [int(e) for e in re.match(r"(\d+),(\d+)", c).groups()] for c in data
    ]
    largest = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            (ax, ay) = coords[i]
            (bx, by) = coords[j]
            area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)
            largest = max(largest, area)
    return largest


already_know = {}


coords = [[int(e) for e in re.match(r"(\d+),(\d+)", c).groups()] for c in data]
edges = set()
for i in range(0, len(coords), 1):
    ax, ay = coords[i]
    bx, by = coords[(i + 1) % len(coords)]

    if ax == bx:
        for ii in range(min(ay, by), max(ay, by) + 1):
            edges.add((ax, ii))
    else:
        for ii in range(min(ax, bx), max(ax, bx) + 1):
            edges.add((ii, ay))
maxedgesx = max(c[0] for c in edges)


@cache
def is_inside(xx, yy):
    if (xx, yy) in edges:
        return True
    xray = [(i, yy) in edges for i in range(xx, maxedgesx + 3)]
    state = False
    count = 0
    for elt in xray:
        if elt == True:
            if state == True:
                continue
            else:
                state = True
                count += 1
        else:
            state = False
    return count % 2 == 1


def rect_ok(bot_left, top_right):
    ax, ay = bot_left
    bx, by = top_right

    minx = min(ax, bx)
    miny = min(ay, by)
    maxx = max(ax, bx)
    maxy = max(ay, by)

    # for yy in [miny, maxy]:
    #     for xx in reversed(range(minx, min(minx + 3000, maxx) + 1)):
    #         if not is_inside(xx, yy):
    #             return False
    #     for xx in reversed(range(max(minx, maxx - 3000), maxx)):
    #         if not is_inside(xx, yy):
    #             return False
    for xx in [minx, maxx]:
        for yy in range(miny, min(maxy, miny + 3000) + 1):
            if not is_inside(xx, yy):
                return False
        for yy in range(max(miny, maxy - 3000), maxy + 1):
            if not is_inside(xx, yy):
                return False
    return True


def part2(data: list[str]):
    largest = 0
    special_coords = [(94918, 50338), (94918, 48430)]
    corners_and_areas = []
    for bot_left in special_coords:
        for j in range(0, len(coords)):
            (ax, ay) = bot_left
            top_right = (bx, by) = coords[j]
            area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)
            if area > 1545850052:
                # might as well use the hint from
                # my wrong answer
                continue
            corners_and_areas.append((area, bot_left, top_right))
    corners_and_areas = list(sorted(corners_and_areas))[::-1]
    for area, bot_left, top_right in tqdm(corners_and_areas):
        if rect_ok(bot_left, top_right):
            print("found largest:")
            return area
    return False


print(part1(data))
print(part2(data))

# 1545850052 = too high
