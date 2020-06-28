# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def mul_of_list(num):
    result = 1
    for i in num:
        result = result * i
    return result


print(mul_of_list((8, 2, 3, -1, 7)))