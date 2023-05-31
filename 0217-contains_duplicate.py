class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe = set(nums)
        return len(nums) != len(dupe)

### NOTES
# a set doesn't contain duplicates