from pathlib import Path

example = Path(__file__).parent / "example.txt"
true_input = Path(__file__).parent / "input.txt"
to_read = true_input

print(f"running with {to_read.name}")
data = open(to_read).read().strip().split("\n")


def match(elt, goal):
    for a, b in zip(elt, goal, strict=True):
        if a != b:
            return False
    return True


def parse(data):
    parsed = []
    for machine in data:
        lights_end = machine.find("]")
        end_buttons = machine.find("{") - 1

        lights = [c for c in machine[1:lights_end]]
        buttons = [
            [int(n) for n in c[1:-1].split(",")]
            for c in machine[lights_end + 2 : end_buttons].split(" ")
        ]
        joltages = [int(c) for c in machine[end_buttons + 1 :][1:-1].split(",")]
        parsed.append((lights, buttons, joltages))
    return parsed


def press_button(state, button):
    new_state = state[:]
    for elt in button:
        if new_state[elt] == ".":
            new_state[elt] = "#"
        else:
            new_state[elt] = "."
    return new_state


def part1(data: list[str]):
    machines = parse(data)

    min_steps = []
    for machine in machines:
        goal = machine[0]
        buttons = machine[1]

        search = [(["." for _ in range(len(goal))], 0, [])]
        min_steps_found = 999999
        already_encountered = {}

        while len(search) > 0:
            state, amount_moves, already_pressed = search.pop(0)
            if amount_moves > min_steps_found:
                continue
            if match(state, goal):
                min_steps_found = min(min_steps_found, amount_moves)
                continue

            key = "".join(state)
            if key in already_encountered:
                if already_encountered[key] <= amount_moves:
                    continue
            already_encountered[key] = amount_moves

            for button in buttons:
                if button in already_pressed:
                    continue
                new_state = press_button(state, button)
                new_moves = amount_moves + 1
                search.append(
                    (
                        new_state,
                        new_moves,
                        already_pressed + [button],
                    )
                )
        min_steps.append(min_steps_found)
    return sum(min_steps)


def part2(data: list[str]):
    pass


print(part1(data))
print(part2(data))
