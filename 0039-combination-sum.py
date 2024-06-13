class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i):
            if i >= len(candidates) or sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            curr.append(candidates[i])
            backtrack(i)
            curr.pop()
            
            backtrack(i + 1)
            
        backtrack(0)
        return res

'''
time complexity of O(2^t) where t is target. You can see t as the height of the decision tree and every level of the tree each branch duplicates.
The thing about this problem is just getting the decision tree down correctly first before coding it
'''
