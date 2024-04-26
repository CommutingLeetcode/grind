# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using fast and slow pointers
        slow = head
        fast = head.next if head else None
        
        # while loop with breaking condition being null is reached
        while(fast):
            if fast == slow:
                return True
            fast = fast.next
            if(fast):
                fast = fast.next
            slow = slow.next
        return False

"""
keep in mind this for this solution, the fast pointer will not meet the slow pointer in the start of the cycle. I would want to make it a standard that when doing a problem like this,
the 2 pointers meet at the start of the cycle. This will be useful for other problems
"""
