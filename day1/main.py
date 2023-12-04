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
        for c in line:
            if c.isnumeric():
                first_digit = c
                break
        for c in reversed(line):
            if c.isnumeric():
                last_digit = c
                break
        if not first_digit or not last_digit:
            raise Exception("No digits found in line")
        line_total = int(f"{first_digit}{last_digit}")
        print(line_total)
        total += line_total
    print(total)


if __name__ == "__main__":
    main()
