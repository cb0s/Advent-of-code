import re


def prepare_inputs(input_values):
    return list(map(int, input_values[0].split(','))),\
           [re.sub(r'\s+', ',', s.strip()) for s in input_values[2:]]   # This is easier to parse later imo


def get_fields(input_values):
    return [[list(map(int, line.split(',')))
             for line in input_values[i:i+5]]
            for i in range(0, len(input_values), 6)]


def calc_final_score(drawing, field):
    return drawing * sum(sum(filter(lambda x: x != -1, l)) for l in field)


def solve_a(input_values: list) -> None:
    bingo_drawings, input_values = prepare_inputs(input_values)
    fields = get_fields(input_values)

    for drawing in bingo_drawings:                              # n iterations
        # mark every field
        for field_index in range(len(fields)):                  # m iterations
            for x in range(len(fields[field_index])):           # 5 iterations
                for y in range(len(fields[field_index][0])):    # 5 iterations
                    if fields[field_index][x][y] == drawing:
                        fields[field_index][x][y] = -1

        # check fields for bingo
        for field_index in range(len(fields)):                  # m iterations
            for x in range(len(fields[field_index])):           # 5 iterations
                possible = [True, True]     # We only check rows and columns -> diagonals are not important
                for y in range(len(fields[field_index][0])):    # 5 iterations
                    possible[0] = possible[0] and fields[field_index][x][y] == -1
                    possible[1] = possible[1] and fields[field_index][y][x] == -1

                if any(possible):
                    log_a("Bingo for field", field_index, "for drawing", drawing)
                    log_a("Final score", calc_final_score(drawing, fields[field_index]))
                    return


def solve_b(input_values: list) -> None:
    bingo_drawings, input_values = prepare_inputs(input_values)
    fields = get_fields(input_values)

    ignore_fields = []

    for drawing in bingo_drawings:                              # n iterations
        # mark every field
        for field_index in range(len(fields)):                  # m iterations
            if field_index in ignore_fields:
                continue

            for x in range(len(fields[field_index])):           # 5 iterations
                for y in range(len(fields[field_index][0])):    # 5 iterations
                    if fields[field_index][x][y] == drawing:
                        fields[field_index][x][y] = -1

        # check fields for bingo
        for field_index in range(len(fields)):                  # m iterations
            if field_index in ignore_fields:
                continue

            for x in range(len(fields[field_index])):           # 5 iterations
                possible = [True, True]     # We only check rows and columns -> diagonals are not important
                for y in range(len(fields[field_index][0])):    # 5 iterations
                    possible[0] = possible[0] and fields[field_index][x][y] == -1
                    possible[1] = possible[1] and fields[field_index][y][x] == -1

                if any(possible):
                    ignore_fields.append(field_index)
                    break

        if len(ignore_fields) == len(fields):
            field_index = next(reversed(ignore_fields))
            log_b("Last bingo will happen for field", field_index)
            log_b("It has a score of", calc_final_score(drawing, fields[field_index]))
            return


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


DAY = 4     # Day of calendar


if __name__ == '__main__':
    main()
