import re

def main():
    # maps = [
    #     'RL',
    #     '',
    #     'AAA = (BBB, CCC)',
    #     'BBB = (DDD, EEE)',
    #     'CCC = (ZZZ, GGG)',
    #     'DDD = (DDD, DDD)',
    #     'EEE = (EEE, EEE)',
    #     'GGG = (GGG, GGG)',
    #     'ZZZ = (ZZZ, ZZZ)'
    # ]
    with open('../data/day08.txt', 'r') as file:
        maps = file.read().splitlines()

    instructions = maps[0].replace('L', '0').replace('R', '1')
    network = [m.split(' = ') for m in maps[2:]]
    d_network = {n[0]: n[1].strip('()').split(', ') for n in network}

    not_at_zzz = True
    current_node = 'AAA'
    num_steps = 0
    while not_at_zzz:
        for instruc in instructions:
            current_node = d_network[current_node][int(instruc)]
            num_steps += 1
            if current_node == 'ZZZ':
                not_at_zzz = False
                break
    print(f'Part 1: {num_steps}')

if __name__ == '__main__':
    main()
