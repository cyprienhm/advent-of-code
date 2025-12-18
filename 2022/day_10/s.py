from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def get_signal(cycle, X):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * X
    return 0


def part1(data: list[str]):
    instructions = [c.split(" ") for c in data]
    X = 1
    cycle = 0
    signal = 0
    for instr in instructions:
        match instr:
            case ["addx", amount]:
                cycle += 1
                signal += get_signal(cycle, X)
                cycle += 1
                signal += get_signal(cycle, X)
                amount = int(amount)
                X += amount
            case ["noop"]:
                cycle += 1
                signal += get_signal(cycle, X)

    return signal


grid_rows = 6
grid_cols = 40


def draw(grid, cycle, X):
    cycle -= 1
    mod40 = cycle % grid_cols
    if X in [mod40 - 1, mod40, mod40 + 1]:
        grid[cycle // 40][cycle % 40] = "#"


def part2(data: list[str]):
    instructions = [c.split(" ") for c in data]
    X = 1
    cycle = 0
    grid = [["." for _ in range(grid_cols)] for _ in range(grid_rows)]
    for instr in instructions:
        match instr:
            case ["addx", amount]:
                cycle += 1
                draw(grid, cycle, X)
                cycle += 1
                draw(grid, cycle, X)
                amount = int(amount)
                X += amount
            case ["noop"]:
                cycle += 1
                draw(grid, cycle, X)

    return "\n".join(["".join(c) for c in grid])


print(part1(data))
print(part2(data))
