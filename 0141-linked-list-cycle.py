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
