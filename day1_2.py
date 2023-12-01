def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    calibration = []

    lines = txt.split("\n")
    for line in lines:
        num = ""

        first = False
        last = ""

        # PART 2
        for i in range(len(line)):
            char = line[i]
            numeric = char.isnumeric()
            if not char.isnumeric():
                char = ""
                if line[i:].startswith("one"):
                    numeric = True
                    char += "1"
                elif line[i:].startswith("two"):
                    numeric = True
                    char += "2"
                elif line[i:].startswith("three"):
                    numeric = True
                    char += "3"
                elif line[i:].startswith("four"):
                    numeric = True
                    char += "4"
                elif line[i:].startswith("five"):
                    numeric = True
                    char += "5"
                elif line[i:].startswith("six"):
                    numeric = True
                    char += "6"
                elif line[i:].startswith("seven"):
                    numeric = True
                    char += "7"
                elif line[i:].startswith("eight"):
                    numeric = True
                    char += "8"
                elif line[i:].startswith("nine"):
                    numeric = True
                    char += "9"

            if numeric:
                if not first:
                    first = True
                    num += char
                else:
                    last = char

        num += last

        if len(num) == 1:
            num += num

        calibration.append(int(num))

    print(sum(calibration))

if __name__ == "__main__":
    main()