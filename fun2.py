# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_of_list(num):
    result = 0
    for i in num:
        result += i
    return result


print(sum_of_list((8, 2, 3, 0, 7)))