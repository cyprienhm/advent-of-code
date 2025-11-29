from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip()


def part1(data: str):
    for i in range(len(data)):
        win = data[i : i + 4]
        if len(set(win)) == len(win):
            return i + 4


def part2(data: str):
    for i in range(len(data)):
        win = data[i : i + 14]
        if len(set(win)) == len(win):
            return i + 14


print(part1(data))
print(part2(data))
