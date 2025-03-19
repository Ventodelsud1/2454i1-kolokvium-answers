def is_sorted(nums):
    for i in range(2, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


numbers = [2, 5, 2, 3, 4]
print(is_sorted(numbers))