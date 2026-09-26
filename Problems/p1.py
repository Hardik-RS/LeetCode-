"""
Problem 1
You are given an integer array nums and an integer target.
Find two different indices whose values add up to target.
"""


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