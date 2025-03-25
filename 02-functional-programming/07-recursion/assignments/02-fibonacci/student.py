

def fibonacci(number):
    print("num "+str(number))
    if (number ==0):
        return 0
    if number ==1 :
        return 1
    n =fibonacci(number -1) + fibonacci(number -2)
    print(n)
    return n

    

print(fibonacci(10))