class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for c in s:
            if c not in pair:
                stack.append(c)
            elif not stack or stack.pop() != pair[c]:
                return False
        
        return not stack
                
# Make a dictionary for the parentheses with the closing as the key
# iterate through it and if it's an opening, append. 
# Else, check if it's empty or the popped is not the pair, return False
# After iterating, return true only if empty

# Time complexity: O(n) 
# Space complexity: O(n)
