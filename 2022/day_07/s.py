from collections import defaultdict
from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    fs = defaultdict(list)
    sizes = defaultdict(int)
    cur_path = ()
    listing_dirs = False
    for line in data:
        toks = line.split(" ")
        if toks[0] == "$":  # cmd
            if toks[1] == "cd":
                if toks[2] == "..":
                    cur_path = cur_path[:-1]
                else:
                    cur_path += (toks[2],)

            elif toks[1] == "ls":
                listing_dirs = True
                continue
        if listing_dirs:
            if len(toks) == 3:
                listing_dirs = False
            else:
                if toks[0] == "dir":
                    continue
                fs[cur_path].append({toks[1]: int(toks[0])})

                for i in range(0, len(cur_path)):
                    sizes[cur_path[: i + 1]] += int(toks[0])

    return sum(filter(lambda x: x <= 100000, sizes.values()))


def part2(data: list[str]):
    fs = defaultdict(list)
    sizes = defaultdict(int)
    cur_path = ()
    listing_dirs = False
    for line in data:
        toks = line.split(" ")
        if toks[0] == "$":  # cmd
            if toks[1] == "cd":
                if toks[2] == "..":
                    cur_path = cur_path[:-1]
                else:
                    cur_path += (toks[2],)

            elif toks[1] == "ls":
                listing_dirs = True
                continue
        if listing_dirs:
            if len(toks) == 3:
                listing_dirs = False
            else:
                if toks[0] == "dir":
                    continue
                fs[cur_path].append({toks[1]: int(toks[0])})

                for i in range(0, len(cur_path)):
                    sizes[cur_path[: i + 1]] += int(toks[0])

    taken = sizes[("/",)]
    target = 30000000
    tot = 70000000
    for d in sorted(sizes, key=sizes.get):
        if tot - taken + sizes[d] >= target:
            return sizes[d]


print(part1(data))
print(part2(data))
