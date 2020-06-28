# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

str = input("Enter a sentence")
words = [word for word in str.split(",")]
print(",".join(sorted(list(set(words)))))
