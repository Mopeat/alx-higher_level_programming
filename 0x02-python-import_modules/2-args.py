#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("{} arguments.".format(n - 1))
    elif n == 2:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))

    if n >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
