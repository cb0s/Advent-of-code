def solve_a(input_values: list) -> None:
    depth = 0
    horizontal_pos = 0

    for command in input_values:
        if command[:7] == 'forward':
            horizontal_pos += int(command[8:])
            continue

        if command[:2] == 'up':
            depth -= int(command[3:])
        elif command[:4] == 'down':
            depth += int(command[5:])

        else:
            raise ValueError("Input could not be parsed!")

    log_a(f"Final horizontal position: {horizontal_pos}")
    log_a(f"Final depth: {depth}")
    log_a(f"Product from depth and horizontal position: {depth * horizontal_pos}")


def solve_b(input_values: list) -> None:
    depth = 0
    horizontal_pos = 0
    aim = 0

    for command in input_values:
        if command[:7] == 'forward':
            x = int(command[8:])
            horizontal_pos += x
            depth += aim * x
            continue

        if command[:2] == 'up':
            aim -= int(command[3:])
        elif command[:4] == 'down':
            aim += int(command[5:])

        else:
            raise ValueError("Input could not be parsed!")

    log_b(f"Final horizontal position: {horizontal_pos}")
    log_b(f"Final depth: {depth}")
    log_b(f"Product from depth and horizontal position: {depth * horizontal_pos}")


def get_contents(path: str) -> list[str]:
    with open(path, 'r') as f:
        contents = f.read()
        lines = contents.splitlines(keepends=False)
        return lines


def try_to_float_values(inputs: list[str]) -> list:
    """Converts inputs to floats if possible."""
    if isinstance(inputs[0], str):
        return inputs
    input_values = [float(s) for s in inputs]
    if len(input_values) < 1:
        raise ValueError("Something went wrong during the import of the dataset!")
    return input_values


def log_a(*args, **kwargs):
    print("[A]", *args, **kwargs)


def log_b(*args, **kwargs):
    print("[B]", *args, **kwargs)


def main():
    input_file = "input.txt"
    lines = get_contents(input_file)

    input_values = try_to_float_values(lines)

    solve_a(input_values)
    print() # Easier to distinguish the outputs
    solve_b(input_values)

    print(f"#### Finished for day {DAY} ####")


DAY = 2     # Day of calendar


if __name__ == '__main__':
    main()
