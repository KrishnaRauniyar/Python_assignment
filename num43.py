#  Write a Python program to remove an item from a tuple.

t1 = (1, 2, 3, 4)
i = int(input("Enter the item to delete"))
t = list(t1)
t.remove(i)
print(tuple(t))
