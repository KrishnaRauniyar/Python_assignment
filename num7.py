# Write a Python function that takes a list of words and returns the length of the
# longest one.

def list_of_words(words):
    list = []
    for i in words:
        list.append((len(i), i))
    list.sort()
    return list[-1][1]

print(list_of_words(["power", "beautiful", "clever"]))

