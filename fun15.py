# Write a Python program to filter a list of integers using Lambda

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

