from functools import cmp_to_key
card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

#file = "demo.txt"
file = "live.txt"

hands = [line.split() for line in open(file, "r").read().split("\n") if line]
#print(hands)

def sort_hand(hands_in_order, hand):
    return sorted(hands_in_order, key=lambda x: card_values.index(x[0]))

def grade_hand(hand):
    repeated_cards = {}
    for card in hand:
        repeated_cards[card[0]] = repeated_cards.get(card[0], 0) + 1
    sorted_repeated_cards = sorted(repeated_cards.items(), key=lambda x: x[1], reverse=True)
    max_repeated_card = sorted_repeated_cards[0][1]
    #print(max_repeated_card)
    match max_repeated_card:
        case 5:
            return 7
        case 4:
            return 6
        case 3:
            match sorted_repeated_cards[1][1]:
                case 2:
                    return 5
                case 1:
                    return 4
        case 2:
            match sorted_repeated_cards[1][1]:
                case 2:
                    return 3
                case 1:
                    return 2
        case 1:
            return 1
    return 0

def sort_by_high_card(a, b):
    hand_a, bet_a = a
    hand_b, bet_b = b
    # sort by grade
    if grade_hand(hand_a) != grade_hand(hand_b):
        return grade_hand(hand_a) - grade_hand(hand_b)
    
    # sort by high card if grade is the same
    for i in range(5):
        card_a_value = card_values.index(hand_a[i])
        card_b_value = card_values.index(hand_b[i])
        if card_a_value > card_b_value:
            return -1
        if card_a_value < card_b_value:
            return 1
        if card_a_value == card_b_value:
            continue   
    return -1


hands.sort(key= lambda hand: grade_hand(hand[0]))
#print(hands)

hands.sort(key=cmp_to_key(sort_by_high_card))
#print(hands)

total = 0
rank = 1
for hand, bet in hands:
    grade = grade_hand(hand)
    print(hand, bet, grade)
    total += int(bet) * rank
    rank += 1

print(total)