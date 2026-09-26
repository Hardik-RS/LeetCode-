"""
Problem 2
Given a string s, determine whether it is a palindrome.
A palindrome reads the same forward and backward.
"""

def palindrom(s):
    s=s.lower()
    left=0
    right=(len(s)-1)
    while left < right:
        if s[left].isalnum():
            if s[right].isalnum():            
                if s[left] == s[right]:
                    left +=1
                    right -=1
                    continue            
                else:
                    return False
            right -=1
            continue 
        left +=1
        continue
    return True
print(palindrom("A man, a plan, a canal: Panama"))
print(palindrom("race a car"))
print(palindrom(" "))
print(palindrom("0P"))
print(palindrom("Race Car"))