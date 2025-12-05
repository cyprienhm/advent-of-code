from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n\n")


def part1(data: list[str]):
    ranges = [[int(a) for a in c.split("-")] for c in data[0].split("\n")]
    ingredients = [int(c) for c in data[1].split("\n")]
    count = 0
    for ing in ingredients:
        if any(lo <= ing and ing <= hi for lo, hi in ranges):
            count += 1
    return count


def add_to_ranges(ranges: list[tuple[int, int]], candidate: tuple[int, int]):
    lo, hi = candidate
    new_ranges = ranges[:]
    for i in range(len(ranges)):
        otherlo, otherhi = ranges[i]

        #      ----
        #   ------------
        if otherlo <= lo and hi <= otherhi:
            new_candidate = (otherlo, otherhi)
            new_ranges.pop(i)
            return add_to_ranges(new_ranges, new_candidate)
        # -----------
        #   -----
        if lo <= otherlo and otherhi <= hi:
            new_candidate = (lo, hi)
            new_ranges.pop(i)
            return add_to_ranges(new_ranges, new_candidate)
        # ----
        #         -----
        if hi < otherlo:
            continue
        #         ----
        # -----
        if otherhi < lo:
            continue
        #      -------
        # -------
        if otherhi >= lo and otherlo <= lo:
            new_candidate = (otherlo, hi)
            new_ranges.pop(i)
            return add_to_ranges(new_ranges, new_candidate)
        #   -------
        #      -------
        if lo <= otherlo and lo <= otherhi:
            new_candidate = (lo, otherhi)
            new_ranges.pop(i)
            return add_to_ranges(new_ranges, new_candidate)

    new_ranges.append(candidate)
    return new_ranges


def part2(data: list[str]):
    ranges = [[int(a) for a in c.split("-")] for c in data[0].split("\n")]
    ranges = [(lo, hi) for lo, hi in ranges]

    reduced = []
    for candidate in ranges:
        reduced = add_to_ranges(reduced, candidate)

    return sum(hi - lo + 1 for lo, hi in reduced)


print(part1(data))
print(part2(data))
