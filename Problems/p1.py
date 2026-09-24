def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i


nums = [2, 7, 4, 2, 9, 8, 2]
target = 11

print(twoSum(nums, target))