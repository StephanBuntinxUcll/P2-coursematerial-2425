

def say_hello():
    print("hello")

def repeat(function, n):
    for i in range(0, n):
        function()
    

# print(repeat(say_hello, 9))