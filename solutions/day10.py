import numpy as np

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

def check_point_eligibility(arr, cur_pos, next_pos):
    if arr[next_pos] == '|' and cur_pos[1] == next_pos[1]:
        return True
    if arr[next_pos] == '-' and cur_pos[0] == next_pos[0]:
        return True
    if arr[next_pos] == 'L' and (cur_pos[1] > next_pos[1] or cur_pos[0] < next_pos[0]):
        return True
    if arr[next_pos] == 'J' and (cur_pos[1] < next_pos[1] or cur_pos[0] < next_pos[0]):
        return True
    if arr[next_pos] == '7' and (cur_pos[1] < next_pos[1] or cur_pos[0] > next_pos[0]):
        return True
    if arr[next_pos] == 'F' and (cur_pos[1] > next_pos[1] or cur_pos[0] > next_pos[0]):
        return True
    return False


def find_next_points(arr, steps_from_start, cur_pos):
    # this will return 2 points initially, and 1 point afterwards
    x, y = cur_pos
    surrounding_points = []
    if arr[cur_pos] in ('S', '-', 'J', '7'):
        surrounding_points.append((x, y - 1))
    if arr[cur_pos] in ('S', '-', 'L', 'F'):
        surrounding_points.append((x, y + 1))
    if arr[cur_pos] in ('S', '|', 'L', 'J'):
        surrounding_points.append((x - 1, y))
    if arr[cur_pos] in ('S', '|', '7', 'F'):
        surrounding_points.append((x + 1, y))
    next_points = []
    for next_pos in surrounding_points:
        try:
            eligible = check_point_eligibility(arr, cur_pos, next_pos)
            if eligible and steps_from_start[next_pos] == -1:
                next_points.append(next_pos)
        except IndexError:
            continue
    return next_points


def main():
    # loop = [
    #     '.....',
    #     '.S-7.',
    #     '.|.|.',
    #     '.L-J.',
    #     '.....'
    # ]
    # loop = [
    #     '-L|F7',
    #     '7S-7|',
    #     'L|7||',
    #     '-L-J|',
    #     'L|-JF'
    # ]
    # loop = [
    #     '..F7.',
    #     '.FJ|.',
    #     'SJ.L7',
    #     '|F--J',
    #     'LJ...'
    # ]
    # loop = [
    #     '7-F7-',
    #     '.FJ|7',
    #     'SJLL7',
    #     '|F--J',
    #     'LJ.LJ'
    # ]
    with open('../data/day10.txt', 'r') as f:
        loop = f.read().splitlines()
    loop = np.array([list(row) for row in loop])
    steps_from_start = np.ones(loop.shape) * -1
    start_pos = tuple([x[0] for x in np.where(loop == 'S')])
    steps_from_start[start_pos] = 0
    found_farthest_point = False
    num_steps = 0
    while not found_farthest_point:
        if num_steps == 0:
            next_pos1, next_pos2 = find_next_points(loop, steps_from_start, start_pos)
        else:
            next_pos1 = find_next_points(loop, steps_from_start, pos1)[0]
            next_pos2 = find_next_points(loop, steps_from_start, pos2)[0]
        print(f'next_pos1: {next_pos1} | next_pos2: {next_pos2}')
        num_steps += 1
        if next_pos1 == next_pos2: #and steps_from_start[next_points[0]] == -1:
            steps_from_start[next_pos1] = num_steps
            found_farthest_point = True
        else:
            if steps_from_start[next_pos1] != -1 and steps_from_start[next_pos2] != -1:
                found_farthest_point = True
            else:
                steps_from_start[next_pos1] = num_steps
                pos1 = next_pos1
                steps_from_start[next_pos2] = num_steps
                pos2 = next_pos2
        print(steps_from_start)
    print(f'Part 1: {int(np.max(steps_from_start))}')


if __name__ == '__main__':
    main()
