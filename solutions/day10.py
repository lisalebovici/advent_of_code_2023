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
    # loop = [
    #     '...........',
    #     '.S-------7.',
    #     '.|F-----7|.',
    #     '.||.....||.',
    #     '.||.....||.',
    #     '.|L-7.F-J|.',
    #     '.|..|.|..|.',
    #     '.L--J.L--J.',
    #     '...........',
    # ]
    # loop = [
    #     '..........',
    #     '.S------7.',
    #     '.|F----7|.',
    #     '.||....||.',
    #     '.||....||.',
    #     '.|L-7F-J|.',
    #     '.|..||..|.',
    #     '.L--JL--J.',
    #     '..........',
    # ]
    loop = [
        '.F----7F7F7F7F-7....',
        '.|F--7||||||||FJ....',
        '.||.FJ||||||||L7....',
        'FJL7L7LJLJ||LJ.L-7..',
        'L--J.L7...LJS7F-7L7.',
        '....F-J..F7FJ|L7L7L7',
        '....L7.F7||L7|.L7L7|',
        '.....|FJLJ|FJ|F7|.LJ',
        '....FJL-7.||.||||...',
        '....L---J.LJ.LJLJ...'
    ]
    # with open('../data/day10.txt', 'r') as f:
    #     loop = f.read().splitlines()
    loop = np.array([list(row) for row in loop])
    steps_from_start = np.ones(loop.shape) * -1
    start_pos = tuple([x[0] for x in np.where(loop == 'S')])
    steps_from_start[start_pos] = 0
    found_farthest_point = False
    num_steps = 0
    enclosure = [start_pos]
    while not found_farthest_point:
        if num_steps == 0:
            next_pos1, next_pos2 = find_next_points(loop, steps_from_start, start_pos)
        else:
            next_pos1 = find_next_points(loop, steps_from_start, pos1)[0]
            next_pos2 = find_next_points(loop, steps_from_start, pos2)[0]
        enclosure.append(next_pos1)
        enclosure.append(next_pos2)
        # print(f'next_pos1: {next_pos1} | next_pos2: {next_pos2}')
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
        # print(steps_from_start)
    print(f'Part 1: {int(np.max(steps_from_start))}')
    enclosure = set(enclosure)

    # check if we cross inside enclosure and count points until we cross again
    status = loop.copy()
    inside_loop = False
    loop_status = 'outside_loop'
    steps_on_enclosure = 0
    # on_enclosure = loop[start_pos] in enclosure
    for i in range(loop.shape[0]):
        for j in range(loop.shape[1]):
            cur_pos = (i, j)
            print(f'cur_pos: {cur_pos}')
            # print('** BEFORE **')
            # print(f'inside_loop: {inside_loop}')
            # print(f'steps_on_enclosure: {steps_on_enclosure}')


            # only want to switch to outside loop if steps on enclosure == 1?

            # passing from outside loop to enclosure
            if not inside_loop and cur_pos in enclosure and loop_status == 'outside_loop' and steps_on_enclosure == 0:
                print('CASE 1')
                steps_on_enclosure += 1
                loop_status = 'on_enclosure'
            # passing from enclosure to inside loop
            elif not inside_loop and cur_pos not in enclosure and loop_status == 'on_enclosure' and steps_on_enclosure == 1:
                print('CASE 2')
                inside_loop = True
                steps_on_enclosure = 0
                status[cur_pos] = 'I'
                loop_status = 'inside_loop'
            # staying in loop
            elif inside_loop and cur_pos not in enclosure and loop_status == 'inside_loop' and steps_on_enclosure == 0:
                print('CASE 3')
                status[cur_pos] = 'I'
            # passing from inside loop to enclosure
            elif inside_loop and cur_pos in enclosure and loop_status == 'inside_loop':
                print('CASE 4')
                steps_on_enclosure += 1
                loop_status = 'on_enclosure'
            # passing from enclosure to outside loop
            elif inside_loop and cur_pos not in enclosure and loop_status == 'on_enclosure' and steps_on_enclosure == 1:
                print('CASE 5')
                inside_loop = False
                steps_on_enclosure = 0
                status[cur_pos] = 'O'
                loop_status = 'outside_loop'
            # passing over enclosure but staying in inside loop
            elif inside_loop and cur_pos not in enclosure and loop_status == 'on_enclosure' and steps_on_enclosure > 1:
                print('CASE 6')
                steps_on_enclosure = 0
                loop_status = 'inside_loop'
                status[cur_pos] = 'I'
            # traversing enclosure
            elif cur_pos in enclosure and loop_status == 'on_enclosure' and steps_on_enclosure > 0:
                print('CASE 7')
                steps_on_enclosure += 1
                pass
            elif cur_pos not in enclosure and loop_status == 'on_enclosure' and steps_on_enclosure > 0:
                print('CASE 8')
                steps_on_enclosure = 0
                loop_status = 'outside_loop'
                status[cur_pos] = 'O'
            # outside loop
            else:
                print('CASE 9')
                status[cur_pos] = 'O'
            print('** AFTER **')
            print(f'inside_loop: {inside_loop}')
            print(f'steps_on_enclosure: {steps_on_enclosure}')
            print(f'on_enclosure: {cur_pos in enclosure}')
            print(f'loop_status: {loop_status}')
            print()

            # if cur_pos in enclosure:
            #     steps_on_enclosure += 1

            # # we were outside the enclosure, now we're on it
            # if loop[i, j] in enclosure and not inside_loop and not on_enclosure:
            #     if 
            #     on_enclosure = True
            # # we're traversing the enclosure, haven't passed inside yet
            # if loop[i, j] in enclosure and not inside_loop and on_enclosure:
            #     continue
            # # we were on the enclosure, now we're not
            # if loop[i, j] not in enclosure and not inside_loop and on_enclosure:
            #     on_enclosure = False

    print(status)
    num_tiles_in_loop = np.sum(status == 'I')
    print(f'Part 2: {num_tiles_in_loop}')
    breakpoint()


if __name__ == '__main__':
    main()




# # passing from outside loop to enclosure
# if not inside_loop and cur_pos in enclosure and steps_on_enclosure == 0:
#     print('CASE 1')
#     steps_on_enclosure += 1
#     loop_status = 'on_enclosure'
# # passing from enclosure to inside loop
# elif not inside_loop and cur_pos not in enclosure and steps_on_enclosure == 1:
#     print('CASE 2')
#     inside_loop = True
#     steps_on_enclosure = 0
#     status[cur_pos] = 'I'
#     loop_status = 'inside_loop'
# # staying in loop
# elif inside_loop and cur_pos not in enclosure and steps_on_enclosure == 0:
#     print('CASE 3')
#     status[cur_pos] = 'I'
# # passing from inside loop to enclosure
# elif inside_loop and cur_pos in enclosure:
#     print('CASE 4')
#     steps_on_enclosure += 1
#     loop_status = 'on_enclosure'
# # passing from enclosure to outside loop
# elif inside_loop and cur_pos not in enclosure:
#     print('CASE 5')
#     inside_loop = False
#     steps_on_enclosure = 0
#     status[cur_pos] = 'O'
#     loop_status = 'outside_loop'
# # traversing enclosure
# elif cur_pos in enclosure and steps_on_enclosure > 0:
#     print('CASE 6')
#     steps_on_enclosure += 1
# elif cur_pos not in enclosure and steps_on_enclosure > 0:
#     print('CASE 7')
#     steps_on_enclosure = 0
#     loop_status = 'outside_loop'
# # outside loop
# else:
#     print('CASE 8')
#     status[cur_pos] = 'O'
