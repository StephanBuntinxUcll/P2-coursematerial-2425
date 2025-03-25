
def is_negative(x):
    return x >= 0

def is_two(x):
    return x == 2

def one(x):
    return x > 4

def take_while(xs,condition):
    a = []
    b = []
    for i in range(0,len(xs)):
        if condition(xs[0]) == condition(xs[i]):
            a.append(xs[i])
            print(condition(xs[0]), condition(xs[i]))
        else:
            print(condition(xs[0]), condition(xs[i]))
            b.append(xs[i:])
            break


    return (a,b)

print(take_while([-4, -2, 0, -1, 4, 6],is_negative))
print(take_while([2, 2, 2],is_two))
print(take_while([1, 2, 3, 4, 5, 6],one))