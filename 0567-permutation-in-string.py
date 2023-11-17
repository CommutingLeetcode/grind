class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # length of s1 greater than s2, return false
        if len(s1) > len(s2):
            return False
        
        # define 2 hashmaps for counting number of characters in the window / string    
        firstMap = {}
        secondMap = {}
        
        # iterate through s1 to get initial counts for the 2 hashmaps
        for i in range(len(s1)):
            firstMap[s1[i]] = firstMap.get(s1[i], 0) + 1
            secondMap[s2[i]] = secondMap.get(s2[i], 0) + 1
            
        
        # iterate through the rest of s2 using sliding window comparing the 2 hashmaps every iteration
        l = 0
        for r in range(len(s1), len(s2)):
            # return true if the window is an anagram of s1
            if firstMap == secondMap:
                return True
            
            # update left char count
            secondMap[s2[l]] -= 1
            if secondMap[s2[l]] == 0:
                secondMap.pop(s2[l])
            l += 1
            
            # update right char count
            secondMap[s2[r]] = secondMap.get(s2[r], 0) + 1
            
        if firstMap == secondMap:
            return True
        
        return False

'''
this is a O(26*n) approach, which is not the most optimal and can be improved on by using the variable match the keeps track of all matching counts in the maps (if it ever reaches 26 it'll return true). For this approach we're doing a comparison of maps which could have at most 26 compraisons every map comparison. Meaning O(26) every comparison. 
'''
