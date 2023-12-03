def get_full_number_by_position(lines, x, y):
    # Reads to the left and to the right of the current position to get the full number
    num = ""
    # Read to the left
    for i in range(x, -1, -1):
        if lines[y][i].isnumeric():
            num = lines[y][i] + num
        else:
            break
    # Read to the right
    for i in range(x + 1, len(lines[y])):
        if lines[y][i].isnumeric():
            num += lines[y][i]
        else:
            break

    return int(num)

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 2
    result = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "*":
                continue

            # Check if there are 2 adjacent numbers
            num_adjacent = 0
            numbers = []
            has_up_num = False
            has_down_num = False
            if x + 1 < len(line) and line[x + 1].isnumeric():
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x + 1, y))
            if x - 1 >= 0 and line[x - 1].isnumeric():
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x - 1, y))
            if y + 1 < len(lines) and lines[y + 1][x].isnumeric():
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x, y + 1))
                has_up_num = True
            if y - 1 >= 0 and lines[y - 1][x].isnumeric():
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x, y - 1))
                has_down_num = True
            if x + 1 < len(line) and y + 1 < len(lines) and lines[y + 1][x + 1].isnumeric() and not has_up_num:
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x + 1, y + 1))
            if x - 1 >= 0 and y - 1 >= 0 and lines[y - 1][x - 1].isnumeric() and not has_down_num:
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x - 1, y - 1))
            if x + 1 < len(line) and y - 1 >= 0 and lines[y - 1][x + 1].isnumeric() and not has_down_num:
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x + 1, y - 1))
            if x - 1 >= 0 and y + 1 < len(lines) and lines[y + 1][x - 1].isnumeric() and not has_up_num:
                num_adjacent += 1
                numbers.append(get_full_number_by_position(lines, x - 1, y + 1))

            if num_adjacent == 2:
                result += numbers[0] * numbers[1]

    print(result)



if __name__ == "__main__":

    main()