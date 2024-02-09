def bubble_sort(nums):
    nums=list(nums)
    for _ in range(0,len(nums)-1):
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]

    return nums

print(bubble_sort([1,4,3,2,8,5]))
print(bubble_sort([1,7,3,0,8,5]))

