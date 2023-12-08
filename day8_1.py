def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    # PART 1
    parts = txt.replace("\r", "").split("\n\n")
    instructions = parts[0]
    data = {}
    for line in parts[1].split("\n"):
        line_parts = line.split("=")
        left_right = line_parts[1].strip().replace("(", "").replace(")", "").split(", ")
        data[line_parts[0].strip()] = left_right

    result = 0
    current = "AAA"
    while current != "ZZZ":
        instruction = instructions[result % len(instructions)]
        result += 1
        if instruction == "L":
            current = data[current][0]
        elif instruction == "R":
            current = data[current][1]

    print(result)

if __name__ == "__main__":
    main()