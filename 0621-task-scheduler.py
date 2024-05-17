class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if n is 0, answer is length of array
        if n == 0:
            return len(tasks)
                
        # initialize freq map
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        queue =  collections.deque()
        
        # counter variable
        counter = 0
        
        # while freq
        while maxHeap or queue:
            if maxHeap:
                # we know we want to operate on the top of the heap, pop it, add it to our queue
                top = heapq.heappop(maxHeap) + 1
                if top != 0:
                    queue.append((top, counter + n))
                    
            # we want to push all the due items in the queue
            if queue and queue[0][1] == counter:
                item = queue.popleft()
                heapq.heappush(maxHeap, item[0])
                
            # increment counter
            counter += 1
        
        # return counter
        return counter


'''
time complexity analysis:
intializing the frequency map: O(n)
creating the heap from an array: O(n)
popping and pushing to the heap: O(26) because there is a limit of 26 different heap nodes in the heap (the alphabet)
the while loop goes for O(n)

space complexity analysis:
O(26)
'''
