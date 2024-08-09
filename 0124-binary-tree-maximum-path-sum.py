# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = root.val
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right),0)
            total = leftSum + node.val + rightSum
            self.max = max(self.max, total)

            return max(leftSum + node.val, rightSum + node.val)
        dfs(root)
        return self.max
'''
This is O(n) time complexity because each node is visited exactly once
This is O(n) space complexity because of the recursive call stack depth being n if the tree is skewed
'''
