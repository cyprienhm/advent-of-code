from collections import defaultdict
from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def part1(data: list[str]):
    beam_row = 0
    beam_cols = [data[0].find("S")]
    splitters = {
        (row, col)
        for row, rowelts in enumerate(data)
        for col, elt in enumerate(rowelts)
        if elt == "^"
    }

    splitters_hit = {elt: False for elt in splitters}
    while beam_row < len(data):
        new_beam_cols = []
        new_beam_row = beam_row + 1

        while len(beam_cols) > 0:
            cur_col = beam_cols.pop()
            if (new_beam_row, cur_col) in splitters:
                splitters_hit[(new_beam_row, cur_col)] = True
                new_beam_cols.append(cur_col - 1)
                new_beam_cols.append(cur_col + 1)
            else:
                new_beam_cols.append(cur_col)
        beam_cols = list(set(new_beam_cols))
        beam_row = new_beam_row
    return sum(splitters_hit.values())


def part2(data: list[str]):
    beam_row = 0
    init_col = data[0].find("S")
    splitters = {
        (row, col)
        for row, rowelts in enumerate(data)
        for col, elt in enumerate(rowelts)
        if elt == "^"
    }

    beams_per_col = {init_col: 1}
    while beam_row < len(data):
        new_beam_cols = defaultdict(int)
        new_beam_row = beam_row + 1

        for cur_col, cur_count in beams_per_col.items():
            if (new_beam_row, cur_col) in splitters:
                new_beam_cols[cur_col - 1] += cur_count
                new_beam_cols[cur_col + 1] += cur_count
            else:
                new_beam_cols[cur_col] += cur_count
        beams_per_col = new_beam_cols
        beam_row = new_beam_row
    return sum(beams_per_col.values())


print(part1(data))
print(part2(data))
