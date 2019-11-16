import sys
import getopt
import random


def _fuse_five_SSS():
    success_chance = {'A': 10, 'S': 5, 'SS': 1}
    lucky_chance = {'A': 3, 'S': 5, 'SS': 10}
    jewels_used_A = 0
    jewels_used_S = 0
    jewels_used_SS = 0

    current_jewels_S = 0
    current_jewels_SS = 0
    current_jewels_SSS = 0

    while current_jewels_SSS < 5:
        if current_jewels_SS >= 3:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('SS'), 10)
            current_jewels_SS -= used_jewels
            jewels_used_SS += used_jewels
            current_jewels_SSS += new_jewel
        elif current_jewels_S >= 3:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('S'), 10)
            current_jewels_S -= used_jewels
            jewels_used_S += used_jewels
            current_jewels_SS += new_jewel
        else:
            used_jewels, new_jewel = _fuse_jewel(success_chance.get('A'), 10)
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
    unixOptions = "ho:v"
    gnuOptions = ["help", "output=", "verbose"]

    fullCmdArguments = sys.argv

    # - further arguments
    argumentList = fullCmdArguments[1:]

    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit(2)

    num_runs = 1
    for i in range(num_runs):
        _fuse_five_SSS()


if __name__ == "__main__":
    main()
