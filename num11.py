#  Write a Python program to count the occurrences of each word in a given
# sentence

str = input("Enter the sentence:")
count = dict()
isoWords = str.split()
for i in isoWords:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)