def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    # PART 2
    sequences = [[int(num) for num in line.split()] for line in txt.replace("\r", "").split("\n")]

    result = 0
    for seq in sequences:
        seq_data = [seq]
        while not all([num == 0 for num in seq_data[-1]]):
            new_seq = []
            for i in range(len(seq_data[-1]) - 1):
                new_seq.append(seq_data[-1][i + 1] - seq_data[-1][i])
            seq_data.append(new_seq)

        seq_data.remove(seq_data[-1])

        for i, new_seq in enumerate(seq_data[::-1]):
            if i == len(seq_data) - 1:
                continue
            seq_data[len(seq_data) - 1 - i - 1].insert(0, seq_data[len(seq_data) - 1 - i - 1][0] - new_seq[0])

        result += seq_data[0][0]

    print(result)


if __name__ == "__main__":
    main()