import re

def clean_number_list(listy):
    return set([int(x) for x in re.sub(r' +', ' ', listy).split(' ')])

def main():
    # cards = [
    #     'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    #     'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    #     'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    #     'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    #     'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    #     'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
    # ]
    with open('../data/day04.txt', 'r') as file:
        cards = file.read().splitlines()

    # Part 1
    pattern = r'.*: +([0-9 ]+) \| +([0-9 ]+)'
    card_points = []
    for card in cards:
        winning_numbers, my_numbers = re.search(pattern, card).groups()
        winning_numbers = clean_number_list(winning_numbers)
        my_numbers = clean_number_list(my_numbers)
        overlapping_numbers = winning_numbers.intersection(my_numbers)
        num_overlap = len(overlapping_numbers)
        if num_overlap > 0:
            points = 2**(num_overlap - 1)
            card_points.append(points)
    print(card_points)
    print(sum(card_points))

if __name__ == '__main__':
    main()
