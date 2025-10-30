import sys
from pathlib import Path

example = Path("example.txt")
true_input = Path("input.txt")
to_read = example

if not to_read.exists():
    sys.exit()

data = open(to_read).read().strip().split("\n")


def part1(): ...


def part2(): ...


print(part1())
print(part2())
