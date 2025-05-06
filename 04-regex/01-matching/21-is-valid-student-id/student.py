# Write your code here

import re

def is_valid_student_id(string):
    return  re.fullmatch("[rsRS][0123456789]{7}", string)

