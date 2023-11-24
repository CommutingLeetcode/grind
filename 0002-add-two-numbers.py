# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # do the first iteration (addition of the head) outside of the loop, get the carry value, enter the loop
        addition = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        l3 = ListNode(addition)
        
        # set the iterators, with the iterator of new list lagging 1 position behind
        temp1 = l1.next
        temp2 = l2.next
        temp3 = l3
        
        # while loop to iterate both lists at once and add them
        while(temp1 and temp2):
            # calculating the sum and carries
            addition = (temp1.val + temp2.val + carry) % 10
            carry = (temp1.val + temp2.val + carry) // 10
            
            # initializing the new node
            newNode = ListNode(addition)
            
            # setting the previous node's next to this new node
            temp3.next = newNode

            # iterating
            temp1 = temp1.next
            temp2 = temp2.next
            temp3 = temp3.next
        
        # carry is still needed just for the first iteration of either 2 while loops
        while(temp1):
            addition = (temp1.val + carry) % 10
            carry = (temp1.val + carry) // 10
            newNode = ListNode(addition)
            temp1 = temp1.next
            temp3.next = newNode
            temp3 = temp3.next
        
        while(temp2):
            addition = (temp2.val + carry) % 10
            carry = (temp2.val + carry) // 10
            newNode = ListNode(addition)
            temp2 = temp2.next
            temp3.next = newNode
            temp3 = temp3.next
        
        if carry == 1:
            temp3.next = ListNode(1)
        
            
        return l3
    
'''
this is technically O(n) but the code I wrote isn't the most compact, and there are many repeated lines. Here are some improvements I can make
1. doing the first iteration out of the loop can be resolved by using a dummy node, and using dummy.next as the head
2. you technically don't need the pointer pointing to the head of list 1 and list 2, so we can directly use that as the iterator
3. we can fuse the three while loops into one by using more condition statements inside that one while loop (this will improve your redundancy concern)
'''
