class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force: sort the array in place n^2 big o time
        # how do we know a sequence in consecutive
        # incrementing 1 from the starting value and see if it exists in the nums array
        # duplicates are not important, we only care about unique values in our array
        
        # array is empty
        if len(nums) == 0:
            return 0
        
        # turn array into set
        numsSet = set(nums)
        
        # counter
        maxSequence = 1
        
        # iterate through the set
        for num in numsSet:
            
            # if left neighbour doesn't exist
            if num - 1 not in numsSet:
                counter = 1
                right = num + 1
                
                # investigate the sequence and keep track of the length
                while right in numsSet:
                    counter += 1
                    maxSequence = max(maxSequence, counter)
                    right = right + 1
                
                    
        return maxSequence

  '''
  O(n) time complexity, worst case will be the array being a huge sequence and the starting digit at the end of the array O(2n)
  O(n) space complexity because we're using a hashset
  '''
