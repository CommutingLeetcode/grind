class Solution:
    def trap(self, height: List[int]) -> int:
        # approach 2: O(1) space complexity
        l, r = 0, len(height) - 1
        maxL, maxR, total = height[0], height[-1], 0

        while l < r:
            print(l, r)
            if maxL <= maxR:
                # process the left pointer
                # calculate trapped water
                trapped = maxL - height[l]
                if trapped > 0:
                    total += trapped
                maxL = max(height[l], maxL)
                l += 1
            else:
                # process the right pointer
                trapped = maxR - height[r]
                if trapped > 0:
                    total += trapped
                maxR = max(height[r], maxR)
                r -= 1
        return total

'''
there is a common off by one error if:
- we use l < r as the loop brekaing condition AND increment last
therefore we have to increment first XOR use l <= r.
O(n) time and O(1) space
'''
