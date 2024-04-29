class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # left array is sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m + 1
            # right array is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                
#         def binarySearch(l, r):
#             while(l <= r):
#                 m = (l + r) // 2
#                 if nums[m] == target:
#                     return m
#                 elif nums[m] > target:
#                     r = m - 1
#                 else:
#                     l = m + 1
#             return -1
        
#         l = 0
#         r = len(nums) - 1
#         pivot = -1
#         # array rotated
#         if nums[l] > nums[r]: 
#             # find a pivot using binary search
#             while(l <= r):
#                 m = (l + r) // 2
#                 if nums[m] > nums[m + 1]:
#                     pivot = m
#                     break
#                 elif nums[m] < nums[l]:
#                     r = m - 1
#                 else:
#                     l = m + 1
                    
#         if pivot != -1:
#             l = 0
#             r = pivot
#             # do binary search on left array
#             left = binarySearch(l, r)
#             if left != -1:
#                 return left
            
#             l = pivot + 1
#             r = len(nums) - 1
#             # do binary search on right array
#             right = binarySearch(l, r)
#             return right
            
#         else:
#             # do regular binary search
#             l = 0
#             r = len(nums) - 1
#             # do binary search
#             return binarySearch(l, r)

'''
The uncommented solution is very much simpler, but the commented one is personally more intuitive for me. Both have an O(log n) time complexity
the thing to remember is you have to figure out the edge cases like what if m == l? If there is a comparison that is out of the usual, like
nums[m] >= nums[l], you have to think about the edge cases.
'''
    
