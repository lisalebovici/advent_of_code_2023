def main():
    with open('../data/day01.txt', 'r') as file:
        text = file.read().splitlines()

    mapping = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine'
        ]
    calibrations = []

    for line in text:
        int_min_idx = None
        int_max_idx = None
        int_min_val = None
        int_max_val = None

        for i, c in enumerate(line):
            try:
                int_min_val = int(c)
                int_min_idx = i
                break
            except:
                pass
        for i, c in enumerate(line[::-1]):
            try:
                int_max_val = int(c)
                int_max_idx = len(line) - i - 1
                break
            except:
                pass

        text_min_idx = 999
        text_max_idx = 0
        text_min_val = None
        text_max_val = None

        for m in mapping:
            idx = line.find(m)
            if idx != -1 and idx < text_min_idx:
                text_min_idx = idx
                text_min_val = mapping.index(m)
            ridx = line.rfind(m)
            if ridx != -1 and ridx > text_max_idx:
                text_max_idx = ridx
                text_max_val = mapping.index(m)

        first = text_min_val if text_min_idx < int_min_idx else int_min_val
        last = text_max_val if text_max_idx > int_max_idx else int_max_val
        cal = first * 10 + last
        calibrations.append(cal)

    print(sum(calibrations))

if __name__ == '__main__':
    main()
