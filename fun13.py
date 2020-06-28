# Write a Python program to sort a list of tuples using Lambda.

names = [('ram', 40), ('shyam', 30), ('rahul', 15)]
names.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(names)