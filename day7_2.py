import functools

def get_card_value(card):
    # In part 2, the joker is the weakest card
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 0
    elif card == "T":
        return 10
    else:
        return int(card)

def get_hand_value_for_static_hand(hand):
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

def get_hand_value(hand):
    # Now the joker is a wild card, so we need to try all the possibilities
    # it can take to get the best hand

    # We use get_hand_value_for_static_hand to get the value of the hand and
    # we replace the joker with each of the other cards to see if we can get
    # a better hand

    card_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    joker_indeces = [i for i in range(len(hand[0])) if hand[0][i] == "J"]
    max_value = 0
    # VERY inefficient, but it works
    for i in range(len(card_list) ** len(joker_indeces)):
        # We get the current combination
        current_combination = i
        current_hand = list(hand[0]).copy()
        for j in range(len(joker_indeces)):
            current_hand[joker_indeces[j]] = card_list[current_combination % len(card_list)]
            current_combination //= len(card_list)

        # We get the value of the hand
        current_value = get_hand_value_for_static_hand((current_hand, 0))
        if current_value > max_value:
            max_value = current_value

    return max_value

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

    # PART 2
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands.sort(key=functools.cmp_to_key(compare_hands))

    result = 0
    for i in range(len(hands)):
        result += hands[i][1] * (i + 1)

    print(result)

if __name__ == "__main__":
    main()