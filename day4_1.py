def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 1
    result = 0
    for line in lines:
        data = line.split(": ")[1].strip()
        parts = data.split("|")
        winning_nums = []
        num_matching = 0
        for num in parts[0].strip().split(" "):
            if num == "":
                continue
            winning_nums.append(int(num))

        for num in parts[1].strip().split(" "):
            if num == "":
                continue
            if int(num) in winning_nums:
                num_matching += 1

        if num_matching > 0:
            result += 2 ** (num_matching - 1)

    print(result)

if __name__ == "__main__":
    main()