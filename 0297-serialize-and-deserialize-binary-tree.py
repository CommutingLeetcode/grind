# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
    
        queue = collections.deque()
        queue.append(root)
        string = []
        while queue:
            popped = queue.popleft()
            if popped == None:
                string.append("#")
                continue
            string.append(str(popped.val))
            queue.append(popped.left)
            queue.append(popped.right)

        return ",".join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        array = data.split(',')
        queue = collections.deque()

        root = TreeNode(array[0])
        queue.append(root)
        i = 1

        while i < len(array) and queue:
            popped = queue.popleft()
            if array[i] == "#":
                popped.left = None
            else:
                left = TreeNode(array[i])
                popped.left = left
                queue.append(left)
            i += 1

            if array[i] == "#":
                popped.right = None
            else:
                right = TreeNode(array[i])
                popped.right = right
                queue.append(right)
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
'''
O(n) space and time complexity. Deserializing needs to use a queue just like serializing. This is the BFS approach
'''
