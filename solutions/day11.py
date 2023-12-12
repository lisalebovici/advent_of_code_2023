import itertools
import numpy as np

def main():
    # image = [
    #     '...#......',
    #     '.......#..',
    #     '#.........',
    #     '..........',
    #     '......#...',
    #     '.#........',
    #     '.........#',
    #     '..........',
    #     '.......#..',
    #     '#...#.....'
    # ]
    with open('../data/day11.txt', 'r') as f:
        image = f.read().splitlines()

    # expand the universe
    image = np.array([list(row) for row in image])
    galaxy_rows, galaxy_cols =  np.where(image == '#')
    nrow = image.shape[0]
    ncol = image.shape[1]
    rows_to_expand = sorted(list(set(range(nrow)) - set(galaxy_rows)))[::-1]
    cols_to_expand = sorted(list(set(range(ncol)) - set(galaxy_cols)))[::-1]
    # for i in rows_to_expand:
    #     image = np.vstack((image[:i], image[i], image[i:]))
    # nrow = image.shape[0]
    # for j in cols_to_expand:
    #     image = np.hstack((image[:, :j], image[:, j].reshape(nrow, 1), image[:, j:]))
    # ncol = image.shape[1]
    
    # find shortest path between each set of galaxies
    galaxy_locs = list(zip(np.where(image=='#')[0], np.where(image=='#')[1]))
    coord_pairs = list(itertools.combinations_with_replacement(galaxy_locs, 2))
    steps = 0
    num_expansions = 1000000
    for i, (coord1, coord2) in enumerate(coord_pairs):
        min_x = min(coord1[0], coord2[0])
        max_x = max(coord1[0], coord2[0])
        min_y = min(coord1[1], coord2[1])
        max_y = max(coord1[1], coord2[1])
        extra_rows = set(range(min_x, max_x)).intersection(set(rows_to_expand))
        extra_cols = set(range(min_y, max_y)).intersection(set(cols_to_expand))
        steps += (np.abs(coord1[0] - coord2[0])
                    + np.abs(coord1[1] - coord2[1])
                    + len(extra_rows) * (num_expansions - 1)
                    + len(extra_cols) * (num_expansions - 1))
    print(f'Part 2: {steps}')

if __name__ == '__main__':
    main()
