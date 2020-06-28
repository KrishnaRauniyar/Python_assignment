#  Write a Python program to remove the characters which have odd index
# values of a given string.

str = input("Enter a string:")
result = ""
for i in range(len(str)):
    if i % 2 == 0:
        result += str[i]
print(result)
