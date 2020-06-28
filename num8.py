# Write a Python program to remove the nth index character from a nonempty
# string

str = input("Enter a string:")
i = int(input("Enter the index to be removed: "))
print(str[:i] + str[i+1:])
