#!/usr/bin/python3
def maxOfTwoNumber(a, b):
    # code to do
    # compare the two values a and b
    if a > b:
        max = a
    else:
        max = b

    # return the higher of the two numbers
    return max


def main():
    n1 = -3
    n2 = -4
    maximum = maxOfTwoNumber(n1, n2)
    print("maximum of", n1, "and", n2, "is", maximum)

main()