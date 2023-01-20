#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = sys.argv
    i = len(sys.argv)
    if i == 1:
        print('0')
    else:
        sum = 0
        for j in range(1, i):
            sum += int(sys.argv[j])
            j += 1
        print("{}".format(sum))
