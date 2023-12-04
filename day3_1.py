def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 1
    result = 0
    num = ""
    num_is_next_to_symbol = False
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (not char.isnumeric()) and num == "":
                continue

            if char.isnumeric():
                num += char
                # Check if the next char is a symbol
                if x + 1 < len(line) and not line[x + 1].isnumeric() and line[x + 1] != ".":
                    num_is_next_to_symbol = True
                elif x - 1 >= 0 and not line[x - 1].isnumeric() and line[x - 1] != ".":
                    num_is_next_to_symbol = True
                elif y + 1 < len(lines) and not lines[y + 1][x].isnumeric() and lines[y + 1][x] != ".":
                    num_is_next_to_symbol = True
                elif y - 1 >= 0 and not lines[y - 1][x].isnumeric() and lines[y - 1][x] != ".":
                    num_is_next_to_symbol = True
                elif x + 1 < len(line) and y + 1 < len(lines) and not lines[y + 1][x + 1].isnumeric() and lines[y + 1][x + 1] != ".":
                    num_is_next_to_symbol = True
                elif x - 1 >= 0 and y - 1 >= 0 and not lines[y - 1][x - 1].isnumeric() and lines[y - 1][x - 1] != ".":
                    num_is_next_to_symbol = True
                elif x + 1 < len(line) and y - 1 >= 0 and not lines[y - 1][x + 1].isnumeric() and lines[y - 1][x + 1] != ".":
                    num_is_next_to_symbol = True
                elif x - 1 >= 0 and y + 1 < len(lines) and not lines[y + 1][x - 1].isnumeric() and lines[y + 1][x - 1] != ".":
                    num_is_next_to_symbol = True

            if (not char.isnumeric() and num != "") or (x == len(line) - 1 and num != ""):
                if num_is_next_to_symbol:
                    result += int(num)
                num = ""
                num_is_next_to_symbol = False

    print(result)

if __name__ == "__main__":
    main()