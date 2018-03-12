#!/bin/python
#ask the user for one number and find all its divisors

def find_devisor(number):
    if number <= 0:
        print("%d should be greater than 0"%(number))
        return 0
    elif number == 1:
        print("1 is the only divisor of 1")
        return 1
    a = range(2,number)
    b = [1,number]
    for n in a:
        if number%n == 0:
            b.append(n)
    b.sort()
    print("the divisor of {0} are: ".format(number))
    print(b)
    return 1

num = int(raw_input("Please enter an integer:"))
while find_devisor(num)!=1:
    num = int(raw_input("Please enter an integer:"))

        
