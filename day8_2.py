from math import lcm

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    # PART 2
    parts = txt.replace("\r", "").split("\n\n")
    instructions = parts[0]
    starting_nodes = []
    data = {}
    for line in parts[1].split("\n"):
        line_parts = line.split("=")
        node = line_parts[0].strip()
        left_right = line_parts[1].strip().replace("(", "").replace(")", "").split(", ")
        if node.endswith("A"):
            starting_nodes.append(node)
        data[node] = left_right

    current_nodes = starting_nodes
    results = []
    for node in current_nodes:
        current = node
        result = 0
        while not current.endswith("Z"):
            instruction = instructions[result % len(instructions)]
            result += 1
            if instruction == "L":
                current = data[current][0]
            elif instruction == "R":
                current = data[current][1]

        results.append(result)

    print(lcm(*results))

if __name__ == "__main__":
    main()