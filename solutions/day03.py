import re


def check_left_and_right(substring, left=True):
    pattern = r'([0-9]+)$' if left else r'^([0-9]+)'
    try:
        num = re.search(pattern, substring).group(1)
        return int(num)
    except AttributeError:
        return None


def check_above_and_below(row, idx, numbers):
    left_check = False
    right_check = False
    left_idx = idx - 1
    right_idx = idx + 1
    num = row[idx]
    while (not left_check or not right_check):
        if not left_check:
            try:
                left_char = row[left_idx]
                if left_char in numbers:
                    num = left_char + num
                    left_idx -= 1
                else:
                    left_check = True
            except IndexError:
                left_check = True
        if not right_check:
            try:
                right_char = row[right_idx]
                if right_char in numbers:
                    num = num + right_char
                    right_idx += 1
                else:
                    right_check = True
            except IndexError:
                right_check = True
    return int(num)


def check_diagonals(row, idx, left=True):
    diag = row[max(idx-3,0):idx] if left else row[idx+1:min(idx+4,len(row))]
    return check_left_and_right(diag, left)


def main():
    # schematic = [
    #     '467..114..',
    #     '...*......',
    #     '..35..633.',
    #     '......#...',
    #     '617*......',
    #     '.....+.58.',
    #     '..592.....',
    #     '......755.',
    #     '...$.*....',
    #     '.664.598..'
    # ]

    with open('../data/day03.txt', 'r') as file:
        schematic = file.read().splitlines()

    checks = []
    numbers = [str(x) for x in range(10)]
    nonsymbols = numbers + ['.']
    nrow = len(schematic)
    ncol = len(schematic[0])
    print(nrow)
    print(ncol)

    # Part 1
    for i, row in enumerate(schematic):
        row_check = ''
        for j, char in enumerate(row):
            if char not in numbers:
                row_check += char
                continue
            next_to_symbol = False
            for ii in (i-1, i, i+1):
                for jj in (j-1, j, j+1):
                    try:
                        val = schematic[ii][jj]
                        if val not in nonsymbols:
                            next_to_symbol = True
                            break
                    except IndexError:
                        continue
                if next_to_symbol:
                    break
            row_check += 'T' if next_to_symbol else 'F'
        checks.append(row_check)

    schematic_split = [re.split(r'\D', s) for s in schematic]
    check_split = [re.split(r'[^TF]', c) for c in checks]

    # print(schematic_split)
    # print(check_split)

    part_numbers = []
    for i, row in enumerate(check_split):
        for j, val in enumerate(row):
            if 'T' in val:
                part_number = int(schematic_split[i][j])
                part_numbers.append(part_number)

    print(part_numbers)
    print(sum(part_numbers))

    # Part 2
    gear_ratios = []
    for i, row in enumerate(schematic):
        if '*' not in row:
            continue
        idxs = [j for j, char in enumerate(row) if char == '*']
        for j in idxs:
            adjacent_parts = 0
            adjacent_numbers = []
            # look left and right
            left = check_left_and_right(row[:j], True)
            if left:
                adjacent_parts += 1
                adjacent_numbers.append(left)
            right = check_left_and_right(row[j+1:], False)
            if right:
                adjacent_parts += 1
                adjacent_numbers.append(right)
            # look above and below
            if i > 0:
                above = schematic[i - 1]
                # first look directly above
                if above[j] in numbers:
                    num = check_above_and_below(above, j, numbers)
                    adjacent_parts += 1
                    adjacent_numbers.append(num)
                # otherwise check diagonals
                else:
                    # check left diagonal
                    left_diag = check_diagonals(above, j, True)
                    if left_diag:
                        adjacent_parts += 1
                        adjacent_numbers.append(left_diag)
                    # check right diagonal
                    right_diag = check_diagonals(above, j, False)
                    if right_diag:
                        adjacent_parts += 1
                        adjacent_numbers.append(right_diag)
            if i < nrow - 1:
                below = schematic[i + 1]
                # first look directly below
                if below[j] in numbers:
                    num = check_above_and_below(below, j, numbers)
                    adjacent_parts += 1
                    adjacent_numbers.append(num)
                # otherwise check diagonals
                else:
                    # check left diagonal
                    left_diag = check_diagonals(below, j, True)
                    if left_diag:
                        adjacent_parts += 1
                        adjacent_numbers.append(left_diag)
                    # check right diagonal
                    right_diag = check_diagonals(below, j, False)
                    if right_diag:
                        adjacent_parts += 1
                        adjacent_numbers.append(right_diag)
            if adjacent_parts == 2:
                gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

    print(gear_ratios)
    print(len(gear_ratios))
    print(sum(gear_ratios))


if __name__ == '__main__':
    main()
