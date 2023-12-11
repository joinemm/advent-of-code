def five_of_a_kind(cards: dict):
    return 5 in cards.values()


def four_of_a_kind(cards: dict):
    return 4 in cards.values()


def full_house(cards: dict):
    vals = cards.values()
    return 3 in vals and 2 in vals


def three_of_a_kind(cards: dict):
    vals = cards.values()
    return 3 in vals and 1 in vals


def two_pair(cards: dict):
    vals = list(cards.values())
    return vals.count(2) == 2


def one_pair(cards: dict):
    vals = list(cards.values())
    return 2 in vals and vals.count(1) == 3


def high_card(cards: dict):
    return list(cards.values()).count(1) == 5


def part1(input: str):
    card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_strength = {k: v for v, k in enumerate(reversed(card_types), start=1)}

    hands = []
    for line in input.split("\n"):
        hand, bid = line.split(" ", 1)
        hand_map = {k: 0 for k in card_types}
        for card in hand:
            hand_map[card] += 1

        hand_score = 8
        for hand_type in [
            five_of_a_kind,
            four_of_a_kind,
            full_house,
            three_of_a_kind,
            two_pair,
            one_pair,
            high_card,
        ]:
            if hand_type(hand_map):
                break
            hand_score -= 1

        cards_score = [card_strength[c] for c in hand]
        hands.append((hand_score, cards_score, hand, int(bid)))

    result = 0
    for i, hand in enumerate(sorted(hands), start=1):
        result += i * hand[3]

    return result


def part2(input: str):
    card_types = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    card_strength = {k: v for v, k in enumerate(reversed(card_types), start=1)}

    hands = []
    for line in input.split("\n"):
        hand, bid = line.split(" ", 1)
        hand_map = {k: 0 for k in card_types}
        for card in hand:
            hand_map[card] += 1

        jokers = hand_map.pop("J")
        hand_map[max((v, k) for k, v in hand_map.items())[1]] += jokers
        hand_score = 8
        for hand_type in [
            five_of_a_kind,
            four_of_a_kind,
            full_house,
            three_of_a_kind,
            two_pair,
            one_pair,
            high_card,
        ]:
            if hand_type(hand_map):
                break
            hand_score -= 1

        cards_score = [card_strength[c] for c in hand]
        hands.append((hand_score, cards_score, hand, int(bid)))

    result = 0
    for i, hand in enumerate(sorted(hands), start=1):
        result += i * hand[3]

    return result
