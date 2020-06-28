# Write a Python script to check whether a given key already exists in a
# dictionary.

d = {2:1, 3:2, 5:10}
i = int(input("Input the key to check: "))
if i in d:
    print("Here is the key")
else:
    print("No key")