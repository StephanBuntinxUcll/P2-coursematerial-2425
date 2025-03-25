

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def adult(x):
    return x.age < 18

def partition(ls, condition):
    a= []
    b =[]
    for i in ls:
        if condition(i):
            a.append(i)
        else:
            b.append(i)
    return (a,b)

print(partition([Person("jack", 15), Person("jeff", 23), Person("Jill", 30), Person("sara", 18)], adult))