class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        
        return False
            
# Use Hashset and iterate nums array
# Time: O(n) -> can loop up to n times 
# Space: O(n) -> hashset can contain up to n nums