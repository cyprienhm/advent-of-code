import re
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Callable

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n\n")


@dataclass
class Monkey:
    items: list[int]
    get_worry: Callable[[int], int]
    test: int
    true_case: int
    false_case: int
    inspections: int = 0


def get_worry_function(operations) -> Callable[[int], int]:
    def get_worry(value) -> int:
        match operations[0]:
            case "old":
                x = value
            case n:
                x = int(n)
        match operations[2]:
            case "old":
                y = value
            case n:
                y = int(n)
        match operations[1]:
            case "*":
                res = x * y
            case "+":
                res = x + y
        return res

    return get_worry


def parse(data) -> list[Monkey]:
    monkeys: list[Monkey] = []
    for monkey in data:
        monkey_data = monkey.split("\n")
        starting_items = (
            re.match(r"\s*Starting items: ([\d, ]+)", monkey_data[1])
            .group(1)
            .split(", ")
        )
        starting_items = [int(c) for c in starting_items]
        operations = (
            re.match(r"\s*Operation: new = ([\w \*\d\+]+)", monkey_data[2])
            .group(1)
            .split(" ")
        )

        test = int(
            re.match(r"\s*Test: divisible by (\d+)", monkey_data[3]).group(1)
        )

        true_case = int(
            re.search(r"If true: throw to monkey (\d+)", monkey).group(1)
        )
        false_case = int(
            re.search(r"If false: throw to monkey (\d+)", monkey).group(1)
        )
        monkeys.append(
            Monkey(
                starting_items,
                get_worry_function(operations),
                test,
                true_case,
                false_case,
            )
        )
    return monkeys


def part1(data: list[str]):
    monkeys = parse(data)
    for round in range(20):
        for i, monkey in enumerate(monkeys):
            while len(monkey.items):
                current_item = monkey.items.pop(0)
                monkey.inspections += 1
                worry = monkey.get_worry(current_item)
                worry //= 3
                pass_to = (
                    monkey.true_case
                    if worry % monkey.test == 0
                    else monkey.false_case
                )
                # print(
                #     f"Monkey {i} inspects {current_item} which is now "
                #     f"{worry} and test is {monkey.test} which is "
                #     f"{worry % monkey.test == 0} and passes to "
                #     f"{pass_to}"
                # )
                monkeys[pass_to].items.append(worry)
    n_inspections = sorted([m.inspections for m in monkeys])

    return n_inspections[-1] * n_inspections[-2]


def part2(data: list[str]):
    monkeys = parse(data)
    tot_tests = reduce(lambda x, y: x * y, [m.test for m in monkeys], 1)
    for round in range(10_000):
        for i, monkey in enumerate(monkeys):
            while len(monkey.items):
                current_item = monkey.items.pop(0)
                monkey.inspections += 1
                worry = monkey.get_worry(current_item)
                pass_to = (
                    monkey.true_case
                    if worry % monkey.test == 0
                    else monkey.false_case
                )
                monkeys[pass_to].items.append(worry % tot_tests)
    n_inspections = sorted([m.inspections for m in monkeys])

    return n_inspections[-1] * n_inspections[-2]


print(part1(data))
print(part2(data))
