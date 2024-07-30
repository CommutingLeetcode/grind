class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr = []
        
        def backtrack(i, total):
            if total == target:
                result.append(curr[:])
                return
            
            if total > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, total + curr[-1])
            curr.pop()
                
            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i = i + 1
              
            backtrack(i + 1, total)
            

        backtrack(0, 0)
        return result

'''
the key thing to remember: we should do the case where we include the value FIRST, instead of after skipping the value. This is important because this solution relies on the list being sorted
time complexity O(2^n) because we ultimately have 2 choices (to include or not to include)
space complexity O(
'''
