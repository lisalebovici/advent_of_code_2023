from collections import Counter

CARD_ORDER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def determine_hand_type(cc):
    if 'J' in cc.keys():
        num_j = cc.pop('J')
    else:
        num_j = 0
    card_counts = sorted(list(cc.values()), reverse=True)
    if card_counts:
        max_count = card_counts[0] + num_j
    else:
        max_count = num_j
    if max_count == 5:
        # five of a kind
        return 7
    if max_count == 4:
        # four of a kind
        return 6
    if max_count == 3:
        # need to check between full house and three of a kind
        second_max_count = card_counts[1]
        if second_max_count == 2:
            # full house
            return 5
        else:
            # three of a kind
            return 4
    if max_count == 2:
        # need to check between two pair and two of a kind
        second_max_count = card_counts[1]
        if second_max_count == 2:
            # two pair
            return 3
        else:
            # two of a kind
            return 2
    # high card
    return 1

def add_hand_card_order(hand_info):
    hand = hand_info[1]
    hand_order = [CARD_ORDER.index(h) for h in hand]
    hand_info.extend(hand_order)
    return hand_info

def main():
    # hands_and_bids = [
    #     '32T3K 765',
    #     'T55J5 684',
    #     'KK677 28',
    #     'KTJJT 220',
    #     'QQQJA 483'
    # ]
    with open('../data/day07.txt', 'r') as file:
        hands_and_bids = file.read().splitlines()

    hands = [h.split(' ')[0] for h in hands_and_bids]
    bids = [int(h.split(' ')[1]) for h in hands_and_bids]
    counts = [Counter(h) for h in hands]
    types = [determine_hand_type(c) for c in counts]
    hand_info = [[bids[x], hands[x], types[x]] for x in range(len(hands))]
    hand_ranks = [add_hand_card_order(h) for h in hand_info]
    hand_ranks_sorted = sorted(hand_ranks, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))
    total_winnings = sum([h[0]*(i+1) for i, h in enumerate(hand_ranks_sorted)])
    print(f'Total winnings: {total_winnings}')

if __name__ == '__main__':
    main()
