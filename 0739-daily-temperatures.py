class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while(stack and temp > stack[-1][1]):
                removed = stack.pop()
                diff = i - removed[0]
                output[removed[0]] = diff
            stack.append((i, temp))
        return output

'''
- stack
- pretty easy one, but getting the difference in index is something I couldn't think of myself so it'd be great to remember
- O(n) since we're just iterating through the temperatures list once
- O(n) space for storing the stack
'''
