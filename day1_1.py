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

        # PART 1
        for char in line:
            if char.isnumeric():
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