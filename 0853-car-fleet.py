class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        counter = 0
        latest = 0
        positionSpeed = [(position[i], speed[i]) for i in range(len(position))]
        positionSpeed.sort(reverse = True, key = lambda x : x[0])
        for position, speed in positionSpeed:
            arrivalTime = (target - position) / speed
            if arrivalTime > latest:
                counter += 1
                latest = arrivalTime
            
            
        return counter
'''
time complexity is O(nlogn) because sorted is needed
space complexity is O(1) because we're not using a stack anymore
'''
