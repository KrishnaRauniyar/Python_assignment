#  Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def check_even_list(l):
    d = []
    for i in l:
        if i % 2 == 0:
            d.append(i)
    return d

print(check_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))