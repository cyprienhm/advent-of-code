from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip()


def invalid(n: int):
    ns = str(n)
    for i in range(len(ns)):
        if ns[:i] == ns[i:]:
            return True
    return False


def invalidp2(n: int):
    ns = str(n)
    for i in range(1, len(ns)):
        if len(ns) % i != 0:
            continue

        amount = len(ns) // i

        if all(ns[:i] == ns[rep * i : (rep + 1) * i] for rep in range(amount)):
            return True
    return False


def part1(data: list[str]):
    ranges = [c.strip().split("-") for c in data.split(",")]

    l = []
    for start, end in ranges:
        startn = int(start)
        endn = int(end)
        for n in range(startn, endn + 1):
            if invalid(n):
                l.append(n)
    return sum(l)


def part2(data: list[str]):
    ranges = [c.strip().split("-") for c in data.split(",")]

    l = []
    for start, end in ranges:
        startn = int(start)
        endn = int(end)
        for n in range(startn, endn + 1):
            if invalidp2(n):
                l.append(n)
    return sum(l)


print(part1(data))
print(part2(data))
