# Write a Python program to sort a list of dictionaries using Lambda.

names = [{'ram':40, 'shyam':100, 'rahul':15}, {'ram':50, 'shyam':80, 'rahul':16}]
n = sorted(names, key= lambda x: x['shyam'])
print(n)