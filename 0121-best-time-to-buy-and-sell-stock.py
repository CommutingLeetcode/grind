class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])

        return res

# Sliding window is a technique to reduce nested loop to a single loop
# In here, we can do that by having two pointers
# Right pointer will iterate and if right is lesser than left, left becomes right. This is because we want to have left as the min possible
# Else, just max the current res with diff of prices[r] - prices[l]
# Return res after iteration

# Time Complexity: O(n)
# Space Complexity: O(1)
