class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # best case O(1)
        
        charDictS = dict()
        charDictT = dict()

        for c in s:
            charDictS[c] = 1 + charDictS.get(c, 0)
        
        for c in t:
            charDictT[c] = 1 + charDictT.get(c, 0)
        
        return charDictS == charDictT

# Make a dictionary for each string, make a counter
# Time: O(n) to iterate until len(s) or len(t) times
# Space: O(n) to store the char to dictionary