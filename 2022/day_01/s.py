from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    elves = [[]]
    for c in data:
        if c == "":
            elves.append([])
        else:
            elves[-1].append(int(c))
    return max((sum(elf) for elf in elves))


def part2(data: list[str]):
    elves = [[]]
    for c in data:
        if c == "":
            elves.append([])
        else:
            elves[-1].append(int(c))
    return sum(sorted([sum(elf) for elf in elves])[-3:])


print(part1(data))
print(part2(data))
