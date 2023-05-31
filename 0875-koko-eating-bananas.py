class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        while (l <= r):
            mid = (l + r) // 2
            hours = 0
            for num in piles:
                hours += ceil(num / mid)
            if (hours <= h):
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
#data structure used: binary search
#what's unique about this problem is to figure out the maximum possible value of k, which is the max number of banana in a pile. See logically speaking, if we take the largest pile, we can always eat other piles in an hour. Now that we have a range of numbers for k, we can apply binary search to find the minimum value of k so that koko can eat as slow as possible while being able to finish before the person comes back
