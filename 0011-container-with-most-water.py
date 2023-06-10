class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_size = 0
        l, r = 0, len(height) - 1

        while l < r:
            size = min(height[l], height[r]) * (r - l)
            max_size = max(max_size, size)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_size

# with two pointer, calculate size and max size everytime
# the pointer with minimum height go to the other pointer, repeat until l == r

# Time complexity: O(n)
# Space complexity: O(1)
