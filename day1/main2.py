digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def main():
    with open("input.txt", "r") as f:
        input = f.read()
    lines = input.split("\n")
    total = 0
    for line in lines:
        if line == "":
            continue
        first_digit = ""
        last_digit = ""
        for c_i, c in enumerate(line):
            if c.isnumeric():
                first_digit = c
                break
            for d_i, d in enumerate(digits):
                slice = line[c_i : c_i + len(d)]
                if slice == d:
                    first_digit = d_i + 1
                    break
            if first_digit:
                break
        for c_i, c in enumerate(reversed(line)):
            if c.isnumeric():
                last_digit = c
                break
            character_index = len(line) - c_i - 1
            for d_i, d in enumerate(digits):
                if line[character_index - len(d) + 1 : character_index + 1] == d:
                    last_digit = d_i + 1
                    break
            if last_digit:
                break
        if not first_digit or not last_digit:
            raise Exception("No digits found in line")
        line_total = int(f"{first_digit}{last_digit}")
        print(line_total)
        total += line_total
    print(total)


if __name__ == "__main__":
    main()
