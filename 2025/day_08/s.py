import re
from functools import reduce
from pathlib import Path

import numpy as np

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def pairwise_distance(x: np.ndarray):
    res = np.zeros((x.shape[0], x.shape[0]))
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            if i == j:
                res[i][j] = np.inf
            else:
                res[i][j] = np.sqrt(np.sum((x[i] - x[j]) ** 2))

    return res


def merge_groups(groups, one, other):
    new_groups = []

    merged = set()
    while len(groups) > 0:
        elt = groups.pop()

        if one in elt or other in elt:
            merged |= elt
        else:
            new_groups.append(elt)
    new_groups.append(merged)
    return new_groups


def part1(data: list[str]):
    coords = [
        [int(elt) for elt in re.match(r"(\d+),(\d+),(\d+)", c).groups()]
        for c in data
    ]
    coords = np.array(coords)
    dists = pairwise_distance(coords)

    dists_pairs = {
        (i, j): float(dists[i][j])
        for i in range(len(coords))
        for j in range(i + 1, len(coords))
    }

    groups = [{i} for i in range(len(coords))]
    for number_connected, (pair_i, pair_j) in enumerate(
        sorted(dists_pairs, key=dists_pairs.get)
    ):
        if number_connected == 1000:
            break
        groups = merge_groups(groups, pair_i, pair_j)

    groups_lengths = list(sorted([len(c) for c in groups]))
    top_3 = groups_lengths[-3:]

    return reduce(lambda x, y: x * y, top_3, 1)


def part2(data: list[str]):
    coords = [
        [int(elt) for elt in re.match(r"(\d+),(\d+),(\d+)", c).groups()]
        for c in data
    ]
    coords = np.array(coords)
    dists = pairwise_distance(coords)

    dists_pairs = {
        (i, j): float(dists[i][j])
        for i in range(len(coords))
        for j in range(i + 1, len(coords))
    }

    groups = [{i} for i in range(len(coords))]
    for number_connected, (pair_i, pair_j) in enumerate(
        sorted(dists_pairs, key=dists_pairs.get)
    ):
        groups = merge_groups(groups, pair_i, pair_j)
        if len(groups) == 1:
            return (
                coords[pair_i][0],
                coords[pair_j][0],
                coords[pair_i][0] * coords[pair_j][0],
            )

    groups_lengths = list(sorted([len(c) for c in groups]))
    top_3 = groups_lengths[-3:]

    return reduce(lambda x, y: x * y, top_3, 1)


print(part1(data))
print(part2(data))
