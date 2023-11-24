"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}
        # first pass: to save all the original nodes as a key that points to the new node in a map
        iterator = head
        while(iterator):
            oldToNew[iterator] = Node(iterator.val)
            iterator = iterator.next
        
        # second pass: to link all the new nodes together, utilizing the map
        iterator = head
        while(iterator):
            oldToNew[iterator].next = oldToNew[iterator.next]
            oldToNew[iterator].random = oldToNew[iterator.random]
            iterator = iterator.next
        
        return oldToNew[head]
    
'''
O(n) space and time complexity for using the map and for iterating the list twice
'''
