#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that 
#they will turn 100 years old
#!/usr/bin/python

class Person:
    'This is a person object'
    person_headcount = 0
    year_now = 2018
    def __init__(self,name,age):
        if (isinstance(age,int)):
            self.name = name
            self.age = age
            self.person_headcount += 1
        else:
            print('age value should be explicit integer! use getPerson refill age')
            self.name = name
            self.age = 0

    def getPerson(self,name,age):
        if (isinstance(age,int)):
            self.name = name
            self.age = age
            self.person_headcount += 1
        else:
            print('age value should be explicit integer! use getPerson refill age')

    def putPerson(self):
        print('the person\'s name is %s, now is %d years old'%(self.name,self.age))

    def answer(self):
        if(self.age <= 0):
            print('{:s} is not born yet'.format(self.name))
        else:
            print('Hi {:s}! You will become 100 years old in {:d}'.format(self.name, 2018 + 100 -  self.age ))

def get_info():
    info = {'name':'', 'age':''}
    name = raw_input("Please input person's name:")
    age = int(raw_input("Please input person's age:"))
    info['name'] = name;
    info['age'] = age;
    return info

if Person.__module__ == '__main__':
    p_info = get_info()
    print("name:%s,age:%d"%(p_info['name'], p_info['age']))
    person = Person(p_info['name'],p_info['age'])
    person.putPerson()
    person.answer()
