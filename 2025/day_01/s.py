from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    d = 50
    c = 0
    for instr in data:
        if instr[0] == "L":
            d -= int(instr[1:])
        else:
            d += int(instr[1:])

        d %= 100
        if d == 0:
            c += 1
    return c


def part2(data: list[str]):
    d = 50
    c = 0
    for instr in data:
        if instr[0] == "L":
            for _ in range(int(instr[1:])):
                d -= 1
                if d == 0:
                    c += 1
                if d < 0:
                    d += 100
        else:
            for _ in range(int(instr[1:])):
                d += 1
                if d >= 100:
                    d -= 100
                if d == 0:
                    c += 1

    return c


print(part1(data))
print(part2(data))
