import numpy as np
import re

def main():
    # raw = [
    #     'Time:      7  15   30',
    #     'Distance:  9  40  200',
    # ]

    with open('../data/day06.txt', 'r') as f:
        raw = f.read().splitlines()

    # Part 1
    rdata = [re.sub(' +', ' ', r).split(' ')[1:] for r in raw]
    races = tuple(zip( [int(r) for r in rdata[0]], [int(r) for r in rdata[1]]))
    num_ways_to_win = []
    for i, (time, dist) in enumerate(races):
        dist_traveled = [(time - speed) * speed for speed in range(time + 1)]
        wins = np.sum(np.array(dist_traveled) > dist)
        num_ways_to_win.append(wins)
    print(f'Part 1: {np.prod(num_ways_to_win)}')

    # Part 2
    races = [int(re.sub(' ', '', r).split(':')[1]) for r in raw]
    time = races[0]
    dist = races[1]
    dist_traveled = [(time - speed) * speed for speed in range(time + 1)]
    wins = np.sum(np.array(dist_traveled) > dist)
    print(f'Part 2: {wins}')

if __name__ == '__main__':
    main()
