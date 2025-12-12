from pathlib import Path

import numpy as np

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

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
                region_shape, required = line.split(": ")
                required = [int(c) for c in required.split(" ")]
                regions.append(
                    (
                        tuple([int(c) for c in region_shape.split("x")]),
                        [
                            (req_index, req_amount)
                            for req_index, req_amount in enumerate(required)
                            if req_amount > 0
                        ],
                    )
                )
            else:
                currently_filled = int(line[:-1])
                shapes[currently_filled] = []
        else:
            shapes[currently_filled].append(
                [1 if c == "#" else 0 for c in line]
            )
    for k in shapes:
        shapes[k] = np.array(shapes[k], dtype=int)
    return shapes, regions


def add_shape_to_grid(grid, shape, row, col):
    shape_rows, shape_cols = shape.shape
    new_grid = grid.copy()
    grid_shape_view = new_grid[
        row : row + shape_rows, col : col + shape_cols
    ].view()
    grid_shape_view += shape
    if np.any(grid_shape_view > 1):
        return None
    return new_grid


def can_fit(region_shape, required, shapes):
    grid = np.zeros((region_shape[1], region_shape[0]), dtype=int)
    search = [(grid, required)]
    already_seen = set()
    tot_expl = 0

    while len(search) > 0:
        current_grid, current_req = search.pop()
        tot_expl += 1

        shape_index, shape_amount = current_req[0]
        # try to insert shape and search it
        shape_to_add = shapes[shape_index]
        new_shape_amount = shape_amount - 1
        adding_last = False
        if new_shape_amount == 0:
            if len(current_req) == 1:
                adding_last = True
            else:
                new_req = current_req[1:]
        else:
            new_req = current_req[:]
            new_req[0] = (shape_index, new_shape_amount)
        for diff in get_flips_and_rots(shape_to_add):
            for row in range(0, grid.shape[0] - diff.shape[0] + 1):
                for col in range(0, grid.shape[1] - diff.shape[1] + 1):
                    # print("try to fit")
                    # print(diff)
                    # print("inside")
                    # print(current_grid)
                    # print("at pos")
                    # print(row, col)
                    new_grid = add_shape_to_grid(
                        current_grid,
                        diff,
                        row,
                        col,
                    )

                    if new_grid is not None:
                        if adding_last:
                            print(new_grid)
                            return True
                        key = new_grid.tobytes()
                        if key in already_seen:
                            continue
                        already_seen.add(key)
                        search.append((new_grid, new_req))
    return False


def can_fit_recursive(grid, required):
    shape_index, shape_amount = required[0]
    # try to insert shape and search it
    shape_to_add = shapes[shape_index]
    for diff in get_flips_and_rots(shape_to_add):
        for row in range(0, grid.shape[0] - diff.shape[0] + 1):
            for col in range(0, grid.shape[1] - diff.shape[1] + 1):
                # print("try to fit")
                # print(diff)
                # print("inside")
                # print(current_grid)
                # print("at pos")
                # print(row, col)
                new_grid = add_shape_to_grid(
                    current_grid,
                    diff,
                    row,
                    col,
                )

                if new_grid is not None:
                    key = new_grid.tobytes()
                    if key in already_seen:
                        continue
                    new_shape_amount = shape_amount - 1
                    if new_shape_amount == 0:
                        if len(current_req) == 1:
                            print(new_grid)
                            return True
                        else:
                            new_req = current_req[1:]
                    else:
                        new_req = current_req[:]
                        new_req[0] = (shape_index, new_shape_amount)
                    already_seen.add(key)
                    search.append((new_grid, new_req))
    return False


def part1(data: list[str]):
    shapes, regions = parse(data)
    count = 0
    for region in regions:
        region_shape = region[0]
        required = region[1]
        tot = 0
        for i, req in required:
            tot += req * np.sum(shapes[i])
        print(tot, region_shape[0] * region_shape[1])
        if tot > region_shape[0] * region_shape[1]:
            continue
        else:
            count += 1

        # if can_fit(region_shape, required, shapes):
        #     count += 1
    print(len(regions))
    return count


def part2(data: list[str]):
    pass


print(part1(data))
print(part2(data))
