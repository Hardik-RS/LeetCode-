"""
Problem 5
Given a string s, find the length of the longest substring
without repeating characters.
A substring is a continuous part of a string.
Return the maximum length of such a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        maximum_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1

            if current_length > maximum_length:
                maximum_length = current_length

        return maximum_length

s="bcaabcabb"
obj=Solution()
print(obj.lengthOfLongestSubstring(s))