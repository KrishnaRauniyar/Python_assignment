# Write a Python program to remove a key from a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a = int(input("Enter the key to be removed:"))
if a in d:
    del d[a]

print(d)