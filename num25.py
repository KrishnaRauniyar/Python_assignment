# Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

l1 = [{}, {}, {}]
l2  = [{1,2}, {}, {}]
print(all(not d for d in l1))
print(all(not d for d in l2))
