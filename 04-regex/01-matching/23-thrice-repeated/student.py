# Write your code here

import re

def thrice_repeated(string):
    return re.fullmatch(r"(.^)\1", string)

print(thrice_repeated("aaa"))
