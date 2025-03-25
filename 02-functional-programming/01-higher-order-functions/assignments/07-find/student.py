
# def has_consecutive_characters(x):
#         return lambda x: x >= 3


def find(strings, condition):
    for i in strings:
        if condition(i):
            return i
            
# print(find([1,2,3,4,5], has_consecutive_characters) )           
