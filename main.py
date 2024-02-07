# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#############################################
# def binary_search(key, arr):
#     low = 0
#     high = len(arr)-1
#
#     while low <= high:
#         mid = (low + high)//2
#         guess = arr[mid]
#         if guess == key:
#             print(mid)
#             print("water")
#             return mid
#         if mid > guess:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None


#
# my_list = [1,2,3,4,5,6,7,8,9]
# item = 5
#
# binary_search(item, my_list)
#
# print("Hi")
#
# import math
#
# result = math.log(256,2)
# print(result)


##################  DSA             #########################

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

#################### Python learning #########################

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    print(list(enumerate(s)))
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1





firstUniqChar('water')

firstUniqChar('leetcode')
firstUniqChar('loveleetcode')