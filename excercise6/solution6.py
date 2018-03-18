#!/bin/python
#Ask user for a string and printer out if it is a palindrome

def palindromeCheck(a):
    flag = 1
    list_a = list(a)
    len_a = len(list_a)
    for i in range(0,len_a/2+1):
        if list_a[i] == list_a[len_a-1-i]:
            pass
        else:
            flag = 0
    return flag

a = raw_input("please enter your string:")
if palindromeCheck(a):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome!")
