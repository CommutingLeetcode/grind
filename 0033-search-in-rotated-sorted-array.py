class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
            
        def findPivot():
            if nums[0] <= nums[-1]:
                return 0
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if m < len(nums) - 1 and nums[m] > nums[m + 1]:
                    return m + 1
                elif nums[m] > nums[-1]:
                    l = m + 1
                else:
                    r = m - 1

        # find pivot
        pivotIdx = findPivot()
        # perform binary search left
        resultLeft = binarySearch(0, pivotIdx - 1)
        if resultLeft != -1:
            return resultLeft
        # perform binary search right
        return binarySearch(pivotIdx, len(nums) - 1)
'''
The uncommented solution is very much simpler, but the commented one is personally more intuitive for me. Both have an O(log n) time complexity
the thing to remember is you have to figure out the edge cases like what if m == l? If there is a comparison that is out of the usual, like
nums[m] >= nums[l], you have to think about the edge cases.

edit (Jul 5th 2025):
saved the most intuitive solution. Find pivot using a binary search
'''
    
