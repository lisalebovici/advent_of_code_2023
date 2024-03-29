import datetime
import re

def get_destination_from_source(d_almanac, mapping, source):
    destination = source
    for (dest, src, rng) in d_almanac[mapping]:
        if source >= src and source < src + rng:
            diff = source - src
            destination = dest + diff
    return destination

def get_location(start, end, d_almanac, mappings, m_idx, max_idx, alm_idx):
    mapping = mappings[m_idx]
    d_map = d_almanac[mapping]
    len_map = len(d_map)
    for i, (dest, src, rng) in enumerate(d_map):
        src_end = src + rng - 1
        dest_end = dest + rng - 1
        # scenario 1: there's no overlap, so just continue on to next mapping
        if start > src_end or end < src:
            if i < len_map - 1:
                continue
            if m_idx < max_idx:
                return get_location(start, end, d_almanac, mappings,
                                    m_idx + 1, max_idx, 0)
            else:
                return start
        # scenario 2: the seeds are completely contained in source range,
        # so convert to destination and pass on to the next mapping
        elif src <= start and end <= src_end:
            diff = start - src
            if m_idx < max_idx:
                return get_location(dest + diff, dest + diff + (end - start),
                                    d_almanac, mappings, m_idx + 1,
                                    max_idx, 0)
            else:
                return dest + diff
        # scenario 3: partial overlap over beginning of source range,
        # need to split into two ranges and recurse
        elif start < src and end <= src_end:
            if m_idx < max_idx:
                if i < len_map - 1:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx, max_idx, i + 1),
                               get_location(dest, dest + (end - src), d_almanac,
                                            mappings, m_idx + 1, max_idx, 0))
                else:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx + 1, max_idx, 0),
                               get_location(dest, dest + (end - src), d_almanac,
                                            mappings, m_idx + 1, max_idx, 0))
            else:
                if i < len_map - 1:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx, max_idx, i + 1),
                               dest)
                else:
                    return min(start, dest)
        # scenario 4: partial overlap over end of source range,
        # need to split into two ranges and recurse
        elif src <= start and src_end < end:
            if m_idx < max_idx:
                if i < len_map - 1:
                    return min(get_location(dest + (start - src), dest_end,
                                            d_almanac, mappings, m_idx + 1,
                                            max_idx, 0),
                               get_location(src_end + 1, end, d_almanac, mappings,
                                            m_idx, max_idx, i + 1))
            else:
                if i < len_map - 1:
                    return min(dest + (start - src),
                               get_location(src_end + 1, end, d_almanac, mappings,
                                            m_idx, max_idx, i + 1))
                else:
                    return min(dest + (start - src), src_end + 1)
        # scenario 5: seeds fully contain source range, split into non-
        # overlapping edges and fully contained middle
        else:
            if m_idx < max_idx:
                if i < len_map - 1:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx, max_idx, i + 1),
                               get_location(dest, dest_end, d_almanac, mappings,
                                            m_idx + 1, max_idx, 0),
                               get_location(src_end + 1, end, d_almanac, mappings,
                                            m_idx, max_idx, i + 1))
                else:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx, max_idx, i + 1),
                               get_location(dest, dest_end, d_almanac, mappings,
                                            m_idx + 1, max_idx, 0),
                               get_location(src_end + 1, end, d_almanac, mappings,
                                            m_idx, max_idx, i + 1))
            else:
                if i < len_map - 1:
                    return min(get_location(start, src - 1, d_almanac, mappings,
                                            m_idx, max_idx, i + 1),
                               dest,
                               get_location(src_end + 1, end, d_almanac, mappings,
                                            m_idx, max_idx, i + 1))
                else:
                    return min(start, dest, src_end + 1)


def main():
    with open('../data/day05.txt', 'r') as file:
        temp = file.read().splitlines()

    delimiter = ''
    almanac = []
    temp_list = []
    for i, t in enumerate(temp[1:]):
        if t == delimiter:
            if i > 0:
                almanac.append(temp_list)
                temp_list = []
            continue
        temp_list.append(t)
    almanac.append(temp_list)
    
    d_almanac = {}
    for alm in almanac:
        key = alm[0].replace(' map:', '')
        d_almanac[key] = []
        for row in alm[1:]:
            r = [int(x) for x in row.split(' ')]
            d_almanac[key].append(r)

    mappings = [
        'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
        'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
        'humidity-to-location'
    ]

    # Part 1
    seeds = [int(x) for x in temp[0].split(':')[1].strip().split(' ')]
    locations = []
    for seed in seeds:
        print(f'SEED: {seed}')
        source = seed
        for mapping in mappings:
            destination = get_destination_from_source(d_almanac, mapping, source)
            print(f'mapping: {mapping} | source: {source} | {destination}')
            source = destination
        locations.append(destination)
        print()
    print(f'Part 1 min location: {min(locations)}')

    # Part 2
    seed_starts = [int(x) for x in temp[0].split(':')[1].strip().split(' ')[::2]]
    seed_ranges = [int(x) for x in temp[0].split(':')[1].strip().split(' ')[1::2]]
    seeds2 = list(zip(seed_starts, seed_ranges))
    num_mappings = len(mappings)

    locations2 = []
    start_ts = datetime.datetime.now()
    for seed_start, seed_range in seeds2:
        seed_end = seed_start + seed_range - 1
        min_loc_for_range = get_location(seed_start, seed_end, d_almanac,
                                         mappings, 0, num_mappings - 1, 0)
        locations2.append(min_loc_for_range)
    end_ts = datetime.datetime.now()
    print(locations2)
    print(f'Part 2 min location: {min(locations2)}')
    print(f'Part 2 run time: {(end_ts-start_ts).microseconds/1000} ms')

if __name__ == '__main__':
    main()
