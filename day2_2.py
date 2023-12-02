def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")
    result = 0
    for line in lines:
        # PART 2
        game_parts = line.split(":")[1].strip().split(";")
        for i in range(len(game_parts)):
            game_parts[i] = game_parts[i].strip()

        min_red = 0
        min_green = 0
        min_blue = 0
        for part in game_parts:
            colors = part.split(",")
            for i in range(len(colors)):
                colors[i] = colors[i].strip()

            for color in colors:
                num = int(color.split(" ")[0])
                color_name = color.split(" ")[1]
                if color_name == "red" and num > min_red:
                    min_red = num
                elif color_name == "green" and num > min_green:
                    min_green = num
                elif color_name == "blue" and num > min_blue:
                    min_blue = num

        result += min_red * min_green * min_blue

    print(result)

if __name__ == "__main__":
    main()