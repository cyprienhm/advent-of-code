from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    ans = 0
    for line in data:
        ns = [int(c) for c in line]
        top = 0
        for i in range(len(ns) - 1):
            for j in range(i + 1, len(ns)):
                cur = ns[i] * 10 + ns[j]
                top = max(top, cur)
        ans += top
    return ans


def part2(data: list[str]):
    ans = 0

    ndigits = 12
    for line in data:
        prev = 0
        cur = ""
        for i in range(ndigits):
            # if picking digit 0, must pick best one in
            #                     [0: len(line) - ndigits]
            # if picking digit 1, must pick best one in
            #                     [last_index: len(line) - ndigits - 1]
            to_pick_from = {
                i: c
                for i, c in enumerate(line[prev : len(line) - ndigits + i + 1])
            }
            best_index = max(to_pick_from, key=to_pick_from.get)
            best_digit = to_pick_from[best_index]
            cur += best_digit
            prev += best_index + 1
        ans += int(cur)

    return ans


print(part1(data))
print(part2(data))
