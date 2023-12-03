#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    from sys import argv
    j = len(argv)
    s = j - 1

    if s > 1:
        print("{} arguments:".format(s))
        for i in range(1, s + 1):
            print("{}: {}".format(i, argv[i]))
    elif s == 0:
        print("{} arguments.".format(s))
    else:
        print("{} argument:".format(s))
        print("{}: {}".format(s, argv[1]))
