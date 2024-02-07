"""
We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
We also need to minimize the number of times we access elements from the list.
"""

# def find_number(arr, query):
#     low=len(arr)-1
#     highest=0
#     if not arr:
#         return -1
#     while low <= highest:
#         mid = (low + highest)//2
#         guess = arr[mid]
#         if guess == query:
#             return query
#         if guess > query:
#             low = mid-1
#         if guess < query:
#             highest=mid+1
#     return -1


# ROTATED LISTS
# CHECK NUMBER OF TIMES A LIST WAS RTATED
def find_rotation_count(nums):
    if not nums:
        return 0
    low,high=0,len(nums)-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]>nums[high]:
            low = mid+1
        else:
            high = mid
    return low


# Example usage:
rotated_list = [5, 6, 9, 0, 2, 3, 4]
rotation_count = find_rotation_count(rotated_list)
print(rotation_count)




