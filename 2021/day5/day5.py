from collections import Counter


def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    parts = line.split(' -> ')  # There should be 2 parts otherwise it is not a line of the inputs
    p1 = tuple(map(int, parts[0].split(',')))   # There should only be 2 parts of a point if line is from inputs
    p2 = tuple(map(int, parts[1].split(',')))   # There should only be 2 parts of a point if line is from inputs
    return p1, p2


def solve_a(input_values: list) -> None:
    lines = [parse_line(l) for l in input_values]

    available_points = []

    for l in lines:
        x0, y0 = l[0]
        x1, y1 = l[1]

        if y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                available_points.append((x, y0))
        elif x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                available_points.append((x0, y))
        # We don't look at else, yet

    log_a("Points with at least 2 straight lines overlapping:",
          len(tuple(filter(lambda c: c >= 2, Counter(available_points).values()))))


def solve_b(input_values: list) -> None:
    lines = [parse_line(l) for l in input_values]

    available_points = []

    for l in lines:
        x0, y0 = l[0]
        x1, y1 = l[1]

        if y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                available_points.append((x, y0))
        elif x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                available_points.append((x0, y))
        else:
            x_slope = int((x1 - x0) / abs(x1 - x0))
            y_slope = int((y1 - y0) / abs(y1 - y0))

            for x, y in zip(range(x0, x1 + x_slope, x_slope), range(y0, y1 + y_slope, y_slope)):
                available_points.append((x, y))

    log_b("Points with at least 2 lines overlapping:",
          len(tuple(filter(lambda c: c >= 2, Counter(available_points).values()))))

def get_contents(path: str) -> list[str]:
    with open(path, 'r') as f:
        contents = f.read()
        lines = contents.splitlines(keepends=False)
        return lines


def log_a(*args, **kwargs):
    print("[A]", *args, **kwargs)


def log_b(*args, **kwargs):
    print("[B]", *args, **kwargs)


def main():
    input_file = "input.txt"
    input_values = get_contents(input_file)

    solve_a(input_values)
    print() # Easier to distinguish the outputs
    solve_b(input_values)

    print(f"#### Finished for day {DAY} ####")


DAY = 5     # Day of calendar


if __name__ == '__main__':
    main()
