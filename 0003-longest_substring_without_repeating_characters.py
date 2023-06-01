class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        longest = 0

        for n in s:
            while n in queue:
                queue.pop(0)
            queue.append(n)
            longest = max(longest, len(queue))

        return longest

        
### NOTES
# use a FIFO queue. Some syntax to remember are 
# append and pop, and both require a parameter,
# otherwise pop() will pop from the back. For this 
# implementation, we want to pop first before appending
# so that the duplicate will first be removed, and the 
# newer letter is added to the queue