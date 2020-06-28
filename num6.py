# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


str = input("Enter a String: ")
nt = str.find('not')
pr = str.find('poor')

if pr > nt and nt > 0 and pr > 0:
    str = str.replace(str[nt:(pr + 4)], 'good')
    print(str)
else:
    print(str)
