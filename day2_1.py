def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    lines = txt.split("\n")
    result = 0
    for line in lines:
        # PART 1
        id = int(line.split(":")[0].split(" ")[1])
        game_parts = line.split(":")[1].strip().split(";")
        for i in range(len(game_parts)):
            game_parts[i] = game_parts[i].strip()

        game_possible = True
        for part in game_parts:
            colors = part.split(",")
            for i in range(len(colors)):
                colors[i] = colors[i].strip()
            for color in colors:
                num = int(color.split(" ")[0])
                color_name = color.split(" ")[1]
                if color_name == "red" and num > MAX_RED:
                    game_possible = False
                elif color_name == "green" and num > MAX_GREEN:
                    game_possible = False
                elif color_name == "blue" and num > MAX_BLUE:
                    game_possible = False

        if game_possible:
            result += id

    print(result)

if __name__ == "__main__":
    main()