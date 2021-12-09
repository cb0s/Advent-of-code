def solve_a(input_values: list[float]) -> None:
    increasings = 0
    prev_val = input_values[0]

    for current_val in input_values[1:]:
        if prev_val < current_val:
            increasings += 1

        prev_val = current_val

    log_a("Sonar-sweep:", increasings)


def solve_b(input_values: list[float]) -> None:
    increasings = 0
    prev_sum = sum(input_values[0:3])
    a = 1   # first index of window
    b = 4   # last index of window -> could be replaced with a + 2

    for _ in range(0, len(input_values) - 3):
        current_sum = sum(input_values[a:b])
        if current_sum > prev_sum:
            increasings += 1

        # Prepare next cycle
        a += 1
        b += 1
        prev_sum = current_sum

    log_b("Noise-compensated sonar sweep:", increasings)


def get_contents(path: str) -> list[str]:
    with open(path, 'r') as f:
        contents = f.read()
        lines = contents.splitlines(keepends=False)
        return lines


def to_float_values(inputs: list[str]) -> list:
    """Converts inputs to floats."""
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
    input_values = get_contents(input_file)

    parsed_values = to_float_values(input_values)

    solve_a(parsed_values)
    print() # Easier to distinguish the outputs
    solve_b(parsed_values)

    print(f"#### Finished for day {DAY} ####")


DAY = 1     # Day of calendar


if __name__ == '__main__':
    main()
