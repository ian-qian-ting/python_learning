#!/bin/python
#Ask user for number. print out if it is odd or even.
#decide if the number is a multiple of 4
#decide if a number is evenly divided by another number
class Check:
    'check a number'
    def __init__(self,number):
        self.number1 = number;
        self.number2 = 1;

    def check1(self):
        if (self.number1 % 2 == 0):
            print("%d is an even number"%(self.number1))
        else:
            print("%d is an odd number"%(self.number1))
        if (self.number1 % 4 == 0):
            print("%d is multiple of 4"%(self.number1))
        else:
            print("%d is not multiple of 4"%(self.number1))
        self.number2 = int(raw_input("please input your dividing number:"))
        if (self.number1 % self.number2 == 0):
            print("%d can be evenly divided by %d"%(self.number1, self.number2))
        else:
            print("%d cannot be evenly divided by %d"%(self.number1, self.number2))

def get_number():
    number = int(raw_input("please enter your number:"))
    return number

if Check.__module__ == "__main__":
    no1 = get_number()
    check = Check(no1)
    check.check1()        
