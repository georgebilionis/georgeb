def find_min_with_for_loop(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  

def find_max_with_for_loop(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_for_loop(nums))  

def find_min_with_while_loop(nums):
    minimum = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
        i += 1
    return minimum


nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums)) 

def find_max_with_while_loop(nums):
    maximum = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > maximum:
            maximum = nums[i]
        i += 1
    return maximum


nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_while_loop(nums))  