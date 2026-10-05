"""
Problem 6
Given a string s containing only the characters:
'(', ')', '{', '}', '[' and ']'.
Determine if the input string is valid.
A string is valid if:
1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.
Return True if the string is valid, otherwise return False.
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            if char in "([{":
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0

s='[)]'
obj=Solution()
print(obj.isValid(s))