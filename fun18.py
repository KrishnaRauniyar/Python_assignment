#  Write a Python program to check whether a given string is number or not
# using Lambda.

is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))