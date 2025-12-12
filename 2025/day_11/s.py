from collections import defaultdict
from functools import cache
from pathlib import Path

example = Path(__file__).parent / "example.txt"
example2 = Path(__file__).parent / "example2.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def parse(data):
    graph = defaultdict(list)

    for line in data:
        source, dests = line.split(": ")
        dests = dests.split(" ")
        graph[source].extend(dests)

    return graph


def dfs(g, src, dst):
    search = [src]
    found_paths = 0

    while len(search) > 0:
        pos = search.pop()

        for neighbor in g[pos]:
            if neighbor == dst:
                found_paths += 1
                continue
            search.append(neighbor)

    return found_paths


def part1(data: list[str]):
    g = parse(data)
    found = dfs(g, "you", "out")
    return found


g = parse(data)


@cache
def num_paths(src, dst, wentbyfft=False, wentbydac=False):
    if src == dst:
        return 0
    if dst in g[src]:
        if wentbyfft and wentbydac:
            return 1
        else:
            return 0
    sources_to_dest = []
    for gsrc, gdsts in g.items():
        if dst in gdsts:
            sources_to_dest.append(gsrc)
    return sum(
        [
            num_paths(
                src,
                new_dst,
                wentbyfft or new_dst == "fft",
                wentbydac or new_dst == "dac",
            )
            for new_dst in sources_to_dest
        ]
    )


def part2(data: list[str]):
    return num_paths("svr", "out")


print(part1(data))
print(part2(data))
