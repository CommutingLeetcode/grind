class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]

                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
            
# use a triple pointer. first pointer that iterate normally and inside the iteration. have two-pointers from far-left and far-right to iterate.

# make sure to check edge cases where: the nums are duplicate
# 1. increment the first pointer if the same as before
# 2. increment the left (second) pointer if the same as before after successfully finding the one. Why just after successful? because duplicate wil only be found after something is found.

# Time complexity: O(n^2). the nested loop and each can go full iteration.
# Space complexity: O(1). no space, sorting here will be built-in in-place quick sort
