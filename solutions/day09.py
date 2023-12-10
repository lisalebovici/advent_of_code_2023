import re

def get_next_value(diff_tree, cur_row_idx, prev_row_idx):
    current_row = diff_tree[cur_row_idx]
    previous_row = diff_tree[prev_row_idx]
    cur_row_last_val = current_row[-1]
    if prev_row_idx == len(diff_tree) - 1:
        prev_row_last_val = 0
    else:
        prev_row_last_val = get_next_value(diff_tree,
                                           cur_row_idx + 1,
                                           prev_row_idx + 1)
    return cur_row_last_val + prev_row_last_val

def get_previous_value(diff_tree, cur_row_idx, prev_row_idx):
    current_row = diff_tree[cur_row_idx]
    previous_row = diff_tree[prev_row_idx]
    cur_row_first_val = current_row[0]
    if prev_row_idx == len(diff_tree) - 1:
        prev_row_first_val = 0
    else:
        prev_row_first_val = get_previous_value(diff_tree,
                                               cur_row_idx + 1,
                                               prev_row_idx + 1)
    return cur_row_first_val - prev_row_first_val

def main():
    # history = [
    #     '0 3 6 9 12 15',
    #     '1 3 6 10 15 21',
    #     '10 13 16 21 30 45'
    # ]
    with open('../data/day09.txt', 'r') as f:
        history = f.read().splitlines()

    next_values = []
    previous_values = []
    for line in history:
        data = [int(x) for x in line.split(' ')]
        diff_tree = [data]
        while True:
            diffs = [y - x for x, y in zip(data[:-1], data[1:])]
            diff_tree.append(diffs)
            data = diffs
            if all(d == 0 for d in diffs):
                break
        next_value = get_next_value(diff_tree, 0, 1)
        next_values.append(next_value)
        previous_value = get_previous_value(diff_tree, 0, 1)
        previous_values.append(previous_value)
    print(next_values)
    print(f'Part 1: {sum(next_values)}')
    print(previous_values)
    print(f'Part 2: {sum(previous_values)}')

if __name__ == '__main__':
    main()
