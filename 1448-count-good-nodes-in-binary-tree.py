# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root, value):
            if not root:
                return 0
            currCount = 0
            # check if root.val > value
            if root.val >= value:
                currCount = 1
            value = max(value, root.val)
            return currCount + count(root.left, value) + count(root.right, value)
        return count(root, root.val)
            
                
