class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}
        def recur(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            root = TreeNode(preorder[preStart])
            rootIndex = inorderMap[preorder[preStart]]

            leftTreeSize = rootIndex - inStart

            root.left = recur(preStart + 1,  preStart + leftTreeSize, inStart, rootIndex - 1)
            root.right = recur(preStart + leftTreeSize + 1, preStart + preEnd, rootIndex + 1, inEnd)

            return root

        return recur(0, len(preorder) - 1, 0, len(inorder) - 1)
'''
time complexity is O(n) in this solution. Each node is processed exactly once and eacth process takes O(1) time.
space complexity is at worst O(n) because the recursive call stack could reach n when the tree is skewed
'''
