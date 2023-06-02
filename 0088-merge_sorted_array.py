class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        pos = m+n-1
        
        while j >= 0:
            if nums1[i] > nums2[j] and i >= 0:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1

### NOTES
# We want to use two pointers to keep track of both arrays, and another pointer
# for the bigger array. Since we know that both arrays are sorted, we can start
# iterating from the back, then moving down the pointer of the respective array
# after insterting the value to the big array. An important thing to keep track
# of is the conditions, we want to make sure that i and j are greater than 0
# before aking the comparisons.