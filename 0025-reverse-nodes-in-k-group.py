class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        left = head
        targetHead = head
        previousEnd = None
        
        while True:
            # get right bound
            right = self.getKthNode(left, k)
            if not right:
                if previousEnd:
                    previousEnd.next = left
                break
                
            # preserve next subList
            nextNode = right.next
            
            # break the current subList's connection to next subList
            right.next = None
            
            # reverse a linked list starting from left
            newHead = self.reverseList(left)
            
            # if it's the first subList, set targetHead
            if left == head:
                targetHead = newHead
            
            # connect previous subList to current subList
            if previousEnd:
                previousEnd.next = newHead
            
            # preserve previousEnd
            previousEnd = left
            
            left = nextNode
            
        return targetHead
    
    def getKthNode(self, head, k):
        while head and k > 1:
            head = head.next
            k -= 1
        return head
    
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
'''
prereq = reverse linked list
we want to make it so that the logic of reversing a sub-list and the logic of connecting the the sub-lists are separated. So that we can abstract away reversing the list and focus on the connection logic which is the most complicated logic
time complexity = O(n)
  - reversing a sublist is O(n/k)
  - getting the kth node is O(k)
  - but these 2 functions are not multiplied. It's either k = 1 (call reverse function n times and getKthNode function becomes O(1)) OR k = n and we're reversing 1 time with O(n) time complexity 
space complexity = O(1)
'''
