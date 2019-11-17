import argparse
import random


def _fuse_five_SSS(lucky):
    success_chance = {'A': 10, 'S': 5, 'SS': 1}
    lucky_chance = {'A': 3, 'S': 5, 'SS': 10, 'DEF': 0}
    jewels_used_A = 0
    jewels_used_S = 0
    jewels_used_SS = 0

    current_jewels_S = 0
    current_jewels_SS = 0
    current_jewels_SSS = 0

    while current_jewels_SSS < 5:
        if current_jewels_SS >= 3:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('SS'), lucky_chance.get(lucky))
            current_jewels_SS -= used_jewels
            jewels_used_SS += used_jewels
            current_jewels_SSS += new_jewel
        elif current_jewels_S >= 3:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('S'), lucky_chance.get(lucky))
            current_jewels_S -= used_jewels
            jewels_used_S += used_jewels
            current_jewels_SS += new_jewel
        else:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('A'), lucky_chance.get(lucky))
            jewels_used_A += used_jewels
            current_jewels_S += new_jewel

    file_out = open("log.txt", "w+")
    file_out.write(str(jewels_used_A) + '\n')
    file_out.write(str(jewels_used_S) + '\n')
    file_out.write(str(jewels_used_SS) + '\n')
    file_out.close()


def _fuse_jewel(success, bonus):
    rand = random.random() * 100
    # return number of jewels used, and number of jewels fused
    if rand <= (success + bonus):
        return 3, 1
    else:
        return 2, 0


def main():
    # initiate the parser
    parser = argparse.ArgumentParser(description='This program runs Monte Carlo simulation on fusing jewels and generates a csv file of the results to this directory, or the specified directory')
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-o", "--output", type=str, help="output directory")
    parser.add_argument("-l", "--lucky", type=str, help="lucky jewel to use [A, S, SS]")
    parser.add_argument("num_simulations", type=int, help="number of simulations to run fusing five SSS jewels")

    # read arguments from the command line
    args = parser.parse_args()

    # check for --version or -V
    if args.version:
        print("Version 1.0")
    if args.output:
        print('Outputting file to: ' + args.output)
    if args.lucky:
        if args.lucky not in ['A', 'S', 'SS']:
            exit('Incorrect Lucky Jewel: ' + args.lucky + ' - Expected A, S, or SS')
        lucky_jewel = args.lucky
    else:
        lucky_jewel = 'DEF'

    for i in range(args.num_simulations):
        _fuse_five_SSS(lucky_jewel)


if __name__ == "__main__":
    main()
