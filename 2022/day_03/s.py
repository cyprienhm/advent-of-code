from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    bags = [(c[: l // 2], c[l // 2 :]) for c in data if (l := len(c))]
    shared = [
        tuple(set(a for a in comp1 if a in comp2))[0] for (comp1, comp2) in bags
    ]
    scores = {
        c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, start=1)
    }

    return sum(scores[c] for c in shared)


def part2(data: list[str]):
    groups = [
        (data[i], data[i + 1], data[i + 2]) for i in range(0, len(data), 3)
    ]
    shared = [
        list(set(a for a in bag1 if all(a in other for other in rest_bags)))[0]
        for bag1, *rest_bags in groups
    ]
    scores = {
        c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, start=1)
    }
    return sum(scores[c] for c in shared)


print(part1(data))
print(part2(data))
