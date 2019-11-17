import argparse
import random
import os

def _fuse_five_SSS(lucky, out_file):
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

    out_file.write(str(jewels_used_A) + ', ')
    out_file.write(str(jewels_used_S) + ', ')
    out_file.write(str(jewels_used_SS) + '\n')



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
    parser.add_argument("-o", "--output", type=str, help="output directory")
    parser.add_argument("-l", "--lucky", type=str, help="lucky jewel to use [A, S, SS]")
    parser.add_argument("file_name", type=str, help="name of the file to output to")
    parser.add_argument("num_simulations", type=int, help="number of simulations to run fusing five SSS jewels")

    # read arguments from the command line
    args = parser.parse_args()

    # checks arguments
    if args.lucky:
        if args.lucky not in ['A', 'S', 'SS']:
            exit('Incorrect Lucky Jewel: ' + args.lucky + ' - Expected A, S, or SS')
        lucky_jewel = args.lucky
    else:
        lucky_jewel = 'DEF'
    if args.output:
        print('Outputting {} to: {}'.format(args.file_name, args.output))
        if not os.path.isdir(args.output):
            os.makedirs(args.output)
        full_file = os.path.join(args.output, args.file_name) + '.csv'
    else:
        full_file = args.file_name + '.csv'

    with open(full_file, 'w+') as out_file:
        out_file.write('A jewels, S jewels, SS jewels\n')
        for i in range(args.num_simulations):
            _fuse_five_SSS(lucky_jewel, out_file)
    exit()


if __name__ == "__main__":
    main()
