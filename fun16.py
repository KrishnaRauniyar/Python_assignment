#  Write a Python program to square and cube every number in a given list of
# integers using Lambda.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq = list(map(lambda x: x**2, nums))
print(sq)
q = list(map(lambda x: x**3, nums))
print(q)