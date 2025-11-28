from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    shape_score = {"X": 1, "Y": 2, "Z": 3}
    win = 6
    draw = 3
    lost = 0
    outcomes = {
        "A": {
            "X": draw,
            "Y": win,
            "Z": lost,
        },
        "B": {
            "X": lost,
            "Y": draw,
            "Z": win,
        },
        "C": {
            "X": win,
            "Y": lost,
            "Z": draw,
        },
    }

    battles = [c.split() for c in data]
    score = sum(shape_score[me] + outcomes[other][me] for other, me in battles)
    return score


def part2(data: list[str]):
    win = 6
    draw = 3
    lost = 0
    outcomes = {"X": lost, "Y": draw, "Z": win}
    forced_score = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2,
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        },
    }

    battles = [c.split() for c in data]
    score = sum(forced_score[other][me] + outcomes[me] for other, me in battles)
    return score


print(part1(data))
print(part2(data))
