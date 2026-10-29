#!/usr/bin/python3

def print_add(argv):
    n = len(argv) - 1
    sum = 0
    if n < 1:
        print(n)
    else:
        for i in argv[1:]:
            sum += int(i)
        print(sum)

if __name__ == "__main__":
    import sys
    print_add(sys.argv)
