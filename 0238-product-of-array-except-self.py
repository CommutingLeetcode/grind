class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
# Make a prefix value 1 (identity in product), travese left to right and will multiply prefix with current input AFTER the result item is multiplied with the prefix
# DO a postfix and do the same but from right to left

# Time complexity: O(n) because it's traversing the list twice
# Space complexity: O(n) because return a new array of size input