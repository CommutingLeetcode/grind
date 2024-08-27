# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy = ListNode(-1, None)
        temp = dummy
        
        # append k heads to the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # while heap exists, find min and append to linked list
        while heap:
            (val, i, curr) = heapq.heappop(heap)
            # replace the entry in the heap if applicable
            if curr.next:
                heapq.heappush(heap, (curr.next.val, i, curr.next))
            
            # append to linked list
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next

'''
tc: klogk + nklogk where k is lists.length and n is lists[0].length
sc = k
'''
