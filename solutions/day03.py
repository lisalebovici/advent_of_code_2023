import re

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

    # print(nrow)
    # print(ncol)

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

if __name__ == '__main__':
    main()
