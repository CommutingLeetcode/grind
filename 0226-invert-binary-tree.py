# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

# Check if not root, return None (since it's Optional but also an edge case for this algorithm
# Else, just switch root.left and root.right but by also calling the invertTree again recursively to ensure the childrens are also inverted
# return root

# Time complexity: O(n) for number of nodes
# Space complexity: O(n) because of the recursive stack function calls
