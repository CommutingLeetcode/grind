class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            currMax = max(currMax, sum)
        return currMax

# array and sliding window
# the main thing about this problem is to set sum to 0 (start over) whenever the sum is negative. Think of it like "it's better to start with 0 rather than a negative". 