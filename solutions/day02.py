import re

def parse_cubes(r, color):
    try:
        if color == 'red':
            num = re.search(r'([0-9]+) red', r).group(1)
        elif color == 'green':
            num = re.search(r'([0-9]+) green', r).group(1)
        elif color == 'blue':
            num = re.search(r'([0-9]+) blue', r).group(1)
    except AttributeError:
        num = 0
    return int(num)

def parse_game(game):
    return int(re.search(r'Game ([0-9]+)', game).group(1))

def main():
    with open('../data/day02.txt', 'r') as file:
        text = file.read().splitlines()

    # part 1
    # red_max = 12
    # green_max = 13
    # blue_max = 14
    # valid_games = []

    power_sets = []

    for line in text:
        game, rounds = line.split(': ')
        rounds = rounds.split('; ')

        # part 2
        red_max = 0
        green_max = 0
        blue_max = 0

        # valid_game = True
        for rnd in rounds:
            red = parse_cubes(rnd, 'red')
            green = parse_cubes(rnd, 'green')
            blue = parse_cubes(rnd, 'blue')
            red_max = max(red, red_max)
            green_max = max(green, green_max)
            blue_max = max(blue, blue_max)
            # if red > red_max or green > green_max or blue > blue_max:
                # valid_game = False
                # break
        # if valid_game:
            # game_num = parse_game(game)
            # valid_games.append(game_num)
        power_sets.append(red_max * green_max * blue_max)

    # print(sum(valid_games))
    # print(valid_games)

    print(sum(power_sets))
    print(power_sets)

if __name__ == '__main__':
    main()
