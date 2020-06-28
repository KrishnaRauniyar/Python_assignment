# Write a Python function to find the Max of three numbers.


def max_of_three_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


print(max(2,5,6))