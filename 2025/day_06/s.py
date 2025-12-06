from functools import reduce
from pathlib import Path

import numpy as np

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def multiply(col):
    return reduce(lambda x, y: x * y, col, 1)


def add(col):
    return sum(col)


def part1(data: list[str]):
    data = [[s for s in c.split(" ") if len(s) > 0] for c in data]
    ops = data[-1]
    nums = np.array([[int(c) for c in row] for row in data[:-1]])
    cols = nums.T
    op_to_func = {"+": add, "*": multiply}

    post_ops = [op_to_func[op](col) for op, col in zip(ops, cols)]
    return sum(post_ops)


def part2(data: list[str]):
    ops = [c for c in data[-1].split(" ") if c != ""][::-1]

    target_cols = len([c for c in data[0].split(" ") if c != ""])

    nums = data[:-1]
    num_rows = len(nums)
    num_cols = len(nums[0])
    parsed_nums = []
    currently_filled = []
    for i in range(num_cols - 1, -1, -1):
        cur = ""
        for row in nums:
            cur += row[i]

        cur = cur.strip()
        if len(cur) == 0:
            parsed_nums.append(currently_filled[:])
            currently_filled.clear()
            continue
        else:
            currently_filled.append(int(cur.strip()))
    parsed_nums.append(currently_filled[:])

    op_to_func = {"+": add, "*": multiply}

    post_ops = [op_to_func[op](col) for op, col in zip(ops, parsed_nums)]
    return sum(post_ops)


print(part1(data))
print(part2(data))
