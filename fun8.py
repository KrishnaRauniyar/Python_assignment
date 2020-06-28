#  Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5] 
# Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    l1 = list(set(l))
    return l1

print(unique_list([1,2,3,3,3,3,4,5]))