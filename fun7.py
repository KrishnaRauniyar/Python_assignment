#  Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def lo_up_check(str):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for i in str:
        if i.isupper():
            d["UPPER_CASE"] += 1
        elif i.islower():
            d["LOWER_CASE"] += 1
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])

lo_up_check("I am a Boy")