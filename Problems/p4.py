"""
Problem 4
You are given an integer array nums.
Return True if any value appears at least twice in the array.
Return False if every element in the array is distinct.
"""

class Solution:
    def containsDuplicate(self, nums):

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False

nums=[1,2,3,4,5,6,7,8,9]
num=[1,2,3,4,5,6,7,5]
obj=Solution()
print(obj.containsDuplicate(nums))
print(obj.containsDuplicate(num))
