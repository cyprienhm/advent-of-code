import re
from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().split("\n\n")


def part1(data: list[str]):
    instr = data[1].split("\n")
    instrs = [
        tuple(
            int(elt)
            for elt in re.match(r"move (\d+) from (\d+) to (\d+)", c).groups()
        )
        for c in instr
    ]
    stacks_str = data[0].split("\n")
    n_stacks = (len(stacks_str[-1]) + 1) // 4
    stacks = [
        list(
            filter(
                lambda x: x != "",
                [
                    row[4 * i : 4 * (i + 1)].strip(" ").strip("[").strip("]")
                    for row in stacks_str[:-1]
                ][::-1],
            )
        )
        for i in range(n_stacks)
    ]

    for n, fro, to in instrs:
        for _ in range(n):
            stacks[to - 1].append(stacks[fro - 1].pop())
    return "".join(c[-1] for c in stacks)


def part2(data: list[str]):
    instr = data[1].split("\n")
    instrs = [
        tuple(
            int(elt)
            for elt in re.match(r"move (\d+) from (\d+) to (\d+)", c).groups()
        )
        for c in instr
    ]
    stacks_str = data[0].split("\n")
    n_stacks = (len(stacks_str[-1]) + 1) // 4
    stacks = [
        list(
            filter(
                lambda x: x != "",
                [
                    row[4 * i : 4 * (i + 1)].strip(" ").strip("[").strip("]")
                    for row in stacks_str[:-1]
                ][::-1],
            )
        )
        for i in range(n_stacks)
    ]

    for n, fro, to in instrs:
        to_move = stacks[fro - 1][-n:]
        stacks[fro - 1] = stacks[fro - 1][:-n]
        stacks[to - 1].extend(to_move)
    return "".join(c[-1] for c in stacks)


def print_stacks(stacks):
    res = ""
    for height in range(max(len(c) for c in stacks)):
        cur = ""
        for s in stacks:
            if height >= len(s):
                cur += "   "
            else:
                cur += "[" + s[height] + "]"
        res = cur + "\n" + res
    print(res)


print(part1(data))
print(part2(data))
