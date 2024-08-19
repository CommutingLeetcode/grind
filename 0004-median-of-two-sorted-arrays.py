class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)
        halfLength = totalLength // 2
        isEven = totalLength % 2 == 0
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # binary search on nums1
        l = 0
        r = len(nums1) - 1
        while True:
            m1 = l + (r - l) // 2
            m2 = halfLength - m1 - 2
            left1 = nums1[m1] if m1 >= 0 else float("-infinity")
            left2 = nums2[m2] if m2 >= 0 else float("-infinity")
            right1 = nums1[m1 + 1] if (m1 + 1) < len(nums1) else float("infinity")
            right2 = nums2[m2 + 1] if (m2 + 1) < len(nums2) else float("infinity")
            if left1 <= right2 and left2 <= right1:
                # odd
                if not isEven:
                    return min(right1, right2)
                # even
                if isEven:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                # shift to left
                r = m1 - 1
            elif left2 > right1:
                # shift to right
                l = m1 + 1
'''
this is O(log(min(m, n))) time complexity with O(1) space
important note to do binary search on the smaller array to avoid index out of bounds error
important note to use sentinel values to handle edge cases by using float("inifinity"). This catches partitions at the edge of the array
'''
