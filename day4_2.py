from collections import deque

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 2
    cards = deque(range(len(lines)))
    result = 0

    card_data = []
    for i, line in enumerate(lines):
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

        earned_cards = []
        for j in range(num_matching):
            if i + j < len(lines):
                earned_cards.append(i + j + 1)

        card_data.append(earned_cards)

    while len(cards) > 0:
        card = cards.popleft()
        cards.extend(card_data[card])
        result += 1

    print(result)

if __name__ == "__main__":
    main()