class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        # iterate
        for i, v in enumerate(heights):
            # if greater, append
            if (not stack) or (stack and v >= stack[-1][1]):
                stack.append((i, v))
                continue

            # if smaller
            lastIndex = 0
            while stack and v < stack[-1][1]:
                popIndex, popValue = stack.pop()
                area = (i - popIndex) * popValue
                maxArea = max(maxArea, area)
                lastIndex = popIndex
            
            stack.append((lastIndex, v))

        # clear the stack with index of len(heights)
        while stack:
            popIndex, popValue = stack.pop()
            area = (len(heights) - popIndex) * popValue
            maxArea = max(maxArea, area)     

        return maxArea    
'''
brute force would be O(n^2) time and O(1) space if you just calculate the minimum value so far and multiply by number of iterations, do that for every entery.
using a stack for optimal solution would be o(n) for time and space
very unique algorithm, but using a monotonicly increasing stack. Remember to save the index as well to keep track of width of rectangles. Remember to update index too to keep track of left area
'''
