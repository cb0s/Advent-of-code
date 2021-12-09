def solve_a(input_values: list) -> None:
    # 8 counters
    # each counter gets increased on 1 and decreased on 0
    # if the end-result is > 1 the corresponding bit is 1 else 0
    counters = [0 for _ in range(len(input_values[0]))]

    for byte in input_values:
        for i, bit in enumerate(byte):
            x = int(bit)
            counters[i] += x if x == 1 else -1

    final_string = ''.join("1" if c > 0 else "0" for c in counters)
    inverse = ''.join("0" if c == "1" else "1" for c in final_string)

    gamma = int(final_string, 2)
    epsilon = int(inverse, 2)    # binary inverse

    log_a(f"Byte: {final_string}")
    log_a(f"Inverse-Byte: {inverse}")
    log_a(f"Gamma: {gamma}")
    log_a(f"Epsilon: {epsilon}")
    log_a(f"Final product: {gamma * epsilon}")


def solve_b(input_values: list) -> None:
    # Now apply filters on input_values as often as necessary
    oxygen_gens = input_values[:]
    co2_scrubs = input_values[:]

    count = 0
    modified = False
    while count < len(input_values[0]):
        # Find bit mask
        oxy_count = [c[count] for c in oxygen_gens].count("1")
        co2_count = [c[count] for c in co2_scrubs].count("1")

        most_common_oxy = "0" if oxy_count < len(oxygen_gens) - oxy_count else "1"
        most_common_co2 = "1" if co2_count < len(co2_scrubs) - co2_count else "0"

        # Apply mask
        if len(oxygen_gens) > 1:
            oxygen_gens = [v for v in filter(lambda o: o if o[count] == most_common_oxy else None, oxygen_gens)
                          if v is not None]
            modified = True

        if len(co2_scrubs) > 1:
            co2_scrubs = [v for v in filter(lambda o: o if o[count] == most_common_co2 else None, co2_scrubs)
                         if v is not None]
            modified = True

        if not modified:
            break

        count += 1

    oxygen_gen = int(oxygen_gens[0], 2)
    co2_scrub = int(co2_scrubs[0], 2)

    log_b(f"Oxygen-Bits: {oxygen_gens[0]}")
    log_b(f"CO2-Bits: {co2_scrubs[0]}")

    log_b(f"Oxygen-Reading: {oxygen_gen}")
    log_b(f"CO2-Reading: {co2_scrub}")

    log_b(f"Life-Support-Rating: {oxygen_gen * co2_scrub}")


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


DAY = 3     # Day of calendar


if __name__ == '__main__':
    main()
