# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iterator = head
        prev = None
        while(iterator):
            forward = iterator.next
            iterator.next = prev
            prev = iterator
            iterator = forward
        return prev
"""
O(n), tricky if you don't remember that you need a previous pointer, took me a while to figure out without look at the solution
you need a temp pointer that the curr.next, because we want to change curr.next to our previous pointer
once you know that, all you need to do is to change prev to curr, then sequentially change curr to temp
There's an edge case in the last iteration where I thought the curr node doesn't have a next. But just realized that
if it doesn't have a next, it will default to point to None. So no need to handle that edge case
"""
