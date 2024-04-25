# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        
        def recursive(root: Optional[TreeNode]) -> int:
            #base case, the reason why we're returning -1 is to revert the addition on the most recent call. We want to revert it because this node is null
            if not root:
                return -1

            #create a variable to store the dimater
            d = 0

            #recursive call
            leftDepth = 1 + recursive(root.left)
            rightDepth = 1 + recursive(root.right)

            #add the 2 depths together
            d = leftDepth + rightDepth

            #store it in global variable if bigger than the global variable's current value
            self.val = max(self.val, d)
            
            #return the max depth of left subtree vs. right subtree
            return max(leftDepth, rightDepth)
        
        recursive(root)
        return self.val


'''
The main thing to remember is that the recursive function only returns the max depth from calling itself on its children. But the calculation of the diameter and comparison to get the max is not returned, it's rather done inside the function and stored in a global variable
Time complexity: in a tree of n nodes, the height would be log(n). The recursive function calls each node once in the algorithm, and the processing time for each node would be O(1). in depth 0 = O(1), depth 1 = O(2), depth 3 = O(8), depth log(n) = O(n). If we add them all up it'll have O(n) processing time

Space complexity: depth of the recursive call stack = height of the tree, best case O(log(n)) on balanced trees and worst case O(n) on skewed trees
'''
