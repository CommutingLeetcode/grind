class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        zipped = list(zip(position, speed))
        sortedZipped = sorted(zipped, reverse=True)
        for (position, speed) in sortedZipped:
            #calculate time of arrival of new car
            tNew = (target - position)/speed
            stack.append((position, speed))
            if(len(stack) > 1):
                tTop = (target - stack[-2][0]) / stack[-2][1]
                if(tTop >= tNew):
                    stack.pop()

        return len(stack)

'''
1. harder one for suree, uses stack and lists of tuples (also uses zip here which is really useful)
2. what's unique is using zip to interleave the elements together which is really useful. Also didn't know sorted sorts tuples based on the first element if not given any parameter to key. other than that if you understand the concept it should be pretty easy to compare the time or arrival
3. time complexity is O(nlogn) because sorted is needed
4. space complexity is O(n for the stack)
'''
