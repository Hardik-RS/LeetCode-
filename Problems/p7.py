"""
Problem 7
You are given an array of strings tokens that represents an
arithmetic expression in Reverse Polish Notation.
Evaluate the expression and return the integer result.
Valid operators are:
+, -, *, /
Division between two integers should truncate toward zero.
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))

            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    result = first + second

                elif token == "-":
                    result = first - second

                elif token == "*":
                    result = first * second

                else:
                    result = int(first / second)

                stack.append(result)

        return stack[0]

obj=Solution()
tokens = ["2", "1", "+", "3", "*"]
print(obj.evalRPN(tokens))