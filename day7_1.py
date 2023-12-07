import functools

def get_card_value(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)

def get_hand_value(hand):
    hand_count = {}
    for card in hand[0]:
        if card in hand_count:
            hand_count[card] += 1
        else:
            hand_count[card] = 1

    # Five of a kind
    if 5 in hand_count.values():
        return 6
    # Four of a kind
    elif 4 in hand_count.values():
        return 5
    # Full house
    elif 3 in hand_count.values() and 2 in hand_count.values():
        return 4
    # Three of a kind
    elif 3 in hand_count.values():
        return 3
    # Two pairs
    elif list(hand_count.values()).count(2) == 2:
        return 2
    # One pair
    elif 2 in hand_count.values():
        return 1
    # High card
    else:
        return 0

def compare_hands(hand1, hand2):
    # We count the number of times each card appears in each hand
    hand1_value = get_hand_value(hand1)
    hand2_value = get_hand_value(hand2)

    if hand1_value > hand2_value:
        return 1
    elif hand1_value < hand2_value:
        return -1
    else:
        # We need to compare the cards
        for i in range(len(hand1[0])):
            card1 = get_card_value(hand1[0][i])
            card2 = get_card_value(hand2[0][i])

            if card1 > card2:
                return 1
            elif card1 < card2:
                return -1

def main():
    txt = ""
    with open("input.txt", "r") as f:
        txt = f.read()

    lines = txt.split("\n")

    # PART 1
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands.sort(key=functools.cmp_to_key(compare_hands))

    result = 0
    for i in range(len(hands)):
        result += hands[i][1] * (i + 1)

    print(result)

if __name__ == "__main__":
    main()