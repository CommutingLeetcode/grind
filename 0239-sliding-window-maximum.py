class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0
        deque = collections.deque()

        while r < len(nums):

            if not deque:
                deque.append(r)
                continue

            # pop outdated elements
            if deque[0] < l:
                deque.popleft()

            while deque and nums[r] >= nums[deque[-1]]:
                deque.pop()
            deque.append(r)
            
            # append to output if window is size k
            if r - l + 1 == k:
                output.append(nums[deque[0]])
                l += 1

            r += 1
        
        return output

'''
(O(k) * n - k times) brute force
(O(1) * n - k times) optimized

pattern: if required for greatest or smallest in O(n) think monotonic stack/queue.
In this case, we require a doubly-ended queue because we want O(1) oepration on:
 - popping right (for maintaining a monotonic decreasing)
 - pushing right (for adding new elements with smaller value)
 - popping left (for outdated elements)

'''
