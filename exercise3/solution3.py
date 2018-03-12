#!/bin/python
#take a list, print all elements that are less than 5
#extra:
#print a list that contains first list's all elements that are less than 5
#do it in one line of python
#ask the user for a number and return a list that contains elements in the list that are smaller than the number given

#take a list
a = [1,1,2,4,7,8,5,0,21]
for n in a:
    if n < 5:
        print("{}".format(n))
b = []
for n in a:
    if n < 5:
        b.append(n);
print b

num = int(raw_input("Please enter a number:"))
c = []
for n in a:
    if n < num:
        c.append(n);
print c
