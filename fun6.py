# Write a Python function to check whether a number is in a given range.

def check_number(n):
    if n in range(1,10):
        print("%s is between 1 and 10" %str(n))
    else:
        print("%s is not in between 1 and 10" %str(n))


check_number(5)