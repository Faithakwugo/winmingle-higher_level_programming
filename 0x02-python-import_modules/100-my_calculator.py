#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    n = len(sys.argv) - 1
    operator = ["+", "-", "*", "/"]
    function = [add, sub, mul, div]
        
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])


    if op not in operator:
        print("Unknow operator. Available operators: +, -, * and //")
        sys.exit(1)
    result = function[operator.index(op)](a, b)
    print("{} {} {} = {}".format(a, op, b, result)) 

