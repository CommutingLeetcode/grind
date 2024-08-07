# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle of linked list by fast and slow pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is one before the start of second linked list
        temp = slow.next
        slow.next = None
        slow = temp

        # reverse second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is the head of the second linked list
        # merge 2 lists together (length of first half <= lenght of second half)
        iterator1 = head
        iterator2 = prev
        while(iterator2):
            temp = iterator1.next
            temp2 = iterator2.next
            iterator1.next = iterator2
            iterator2.next = temp
            iterator1 = temp
            iterator2 = temp2
        
        return head

'''
time complexity = O(n)
space complexity = constant
pretty straight forward, watch out for off by one errors and edge cases
'''
