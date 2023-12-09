import math

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
    # maps2 = [
    #     'LR',
    #     '',
    #     '11A = (11B, XXX)',
    #     '11B = (XXX, 11Z)',
    #     '11Z = (11B, XXX)',
    #     '22A = (22B, XXX)',
    #     '22B = (22C, 22C)',
    #     '22C = (22Z, 22Z)',
    #     '22Z = (22B, 22B)',
    #     'XXX = (XXX, XXX)',
    # ]
    with open('../data/day08.txt', 'r') as file:
        maps = file.read().splitlines()

    instructions = maps[0].replace('L', '0').replace('R', '1')
    network = [m.split(' = ') for m in maps[2:]]
    d_network = {n[0]: n[1].strip('()').split(', ') for n in network}

    # Part 1
    not_at_zzz = True
    current_node = 'AAA'
    num_steps = 0
    while not_at_zzz:
        # "repeat the whole sequence of instructions as necessary"
        for i in instructions:
            current_node = d_network[current_node][int(i)]
            num_steps += 1
        # then check if we're at the end node
        if current_node == 'ZZZ':
            not_at_zzz = False
            break
    print(f'Part 1: {num_steps}')

    # Part 2
    a_nodes = [node for node in d_network.keys() if node[-1] == 'A']
    z_nodes = [node for node in d_network.keys() if node[-1] == 'Z']
    current_nodes = a_nodes
    iterations = []
    for current_node in current_nodes:
        print(current_node)
        num_steps2 = 0
        not_at_zzz2 = True
        while not_at_zzz2:
            # "repeat the whole sequence of instructions as necessary"
            for i in instructions:
                current_node = d_network[current_node][int(i)]
                num_steps2 += 1
            # then check if we're at one of the end nodes
            if current_node in z_nodes:
                print(current_node)
                not_at_zzz2 = False
        iters = int(num_steps2 / len(instructions))
        iterations.append(iters)
        print(f'iterations: {iters}')
    num_steps2_total = math.lcm(*iterations) * len(instructions)
    print(f'Part 2: {num_steps2_total}')

if __name__ == '__main__':
    main()
