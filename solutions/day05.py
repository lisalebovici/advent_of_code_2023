import re

def get_destination_from_source(d_almanac, mapping, source):
    destination = source
    for (dest, src, rng) in d_almanac[mapping]:
        if source >= src and source < src + rng:
            diff = source - src
            destination = dest + diff
            # sources = list(range(src, src+rng))
            # dests = list(range(dest, dest+rng))
            # if source in sources:
                # idx = sources.index(source)
                # destination = dests[idx]
                # break
    return destination

def main():
    with open('../data/day05.txt', 'r') as file:
        temp = file.read().splitlines()

    seeds = [int(x) for x in temp[0].split(':')[1].strip().split(' ')]

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

    print(f'Min location: {min(locations)}')

if __name__ == '__main__':
    main()
