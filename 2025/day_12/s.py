from pathlib import Path

import numpy as np

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = example

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def get_flips_and_rots(arr):
    arr = arr
    rot1 = np.rot90(arr)
    rot2 = np.rot90(rot1)
    rot3 = np.rot90(rot2)

    flipped = np.fliplr(arr)
    rot1_flipped = np.rot90(flipped)
    rot2_flipped = np.rot90(rot1_flipped)
    rot3_flipped = np.rot90(rot2_flipped)

    return (
        arr,
        rot1,
        rot2,
        rot3,
        flipped,
        rot1_flipped,
        rot2_flipped,
        rot3_flipped,
    )


def parse(data):
    regions = []
    shapes = {}
    currently_filled = None
    for line in data:
        if len(line) == 0:
            continue
        if ":" in line:
            if "x" in line:
                # final instr
                region_shape, indices = line.split(": ")
                regions.append(
                    (
                        [int(c) for c in region_shape.split("x")],
                        [int(c) for c in indices.split(" ")],
                    )
                )
            else:
                currently_filled = int(line[:-1])
                shapes[currently_filled] = []
        else:
            shapes[currently_filled].append([c for c in line])
    for k in shapes:
        shapes[k] = np.array(shapes[k])
    return shapes, regions


def add_shape_to_grid(grid, shape, row, col):
    new_grid = grid.copy()
    shape_rows, shape_cols = shape.shape
    grid_rows, grid_cols = new_grid.shape
    if row + shape_rows > grid_rows:
        return None
    if col + shape_cols > grid_cols:
        return None
    # if (
    #     new_grid[row : row + shape_rows, col : col + shape_cols].shape
    #     != shape.shape
    # ):
    #     return None

    # shape_mask = shape == "#"
    # grid_shape_view = new_grid[row : row + shape_rows, col : col + shape_cols]
    #
    # if not np.all(grid_shape_view[shape_mask] == "."):
    #     return None
    for i, row_i in enumerate(range(row, row + shape_rows)):
        for j, col_j in enumerate(range(col, col + shape_cols)):
            if shape[i][j] == "#":
                if new_grid[row_i, col_j] == "#":
                    return None
                new_grid[row_i, col_j] = "#"
    return new_grid


def can_fit(region_shape, required, shapes):
    grid = np.array(
        [["." for _ in range(region_shape[0])] for _ in range(region_shape[1])]
    )
    search = [(grid, required)]
    already_seen = set()
    tot_expl = 0

    while len(search) > 0:
        current_grid, current_req = search.pop()
        tot_expl += 1

        for shape_index, shape_amount in enumerate(current_req):
            if shape_amount > 0:
                shape_to_add_index = shape_index
                break

        # try to insert shape and search it
        shape_to_add = shapes[shape_to_add_index]
        for diff in get_flips_and_rots(shape_to_add):
            for row in range(0, region_shape[1] - diff.shape[0] + 1):
                for col in range(0, region_shape[0] - diff.shape[1] + 1):
                    # print("try to fit")
                    # print(diff)
                    # print("inside")
                    # print(current_grid)
                    # print("at pos")
                    # print(row, col)
                    res = add_shape_to_grid(
                        current_grid,
                        diff,
                        row,
                        col,
                    )

                    if res is not None:
                        new_req = current_req[:]
                        new_req[shape_index] -= 1
                        if all(c == 0 for c in new_req):
                            print(res)
                            return True
                        key = "".join(
                            ["".join([c for c in row]) for row in res]
                        )
                        if key in already_seen:
                            continue
                        already_seen.add(key)
                        search.append((res, new_req))
    return False


def part1(data: list[str]):
    shapes, regions = parse(data)
    count = 0
    for region in regions:
        shape = region[0]
        required = region[1]
        if can_fit(shape, required, shapes):
            count += 1
    return count


def part2(data: list[str]):
    pass


print(part1(data))
print(part2(data))
