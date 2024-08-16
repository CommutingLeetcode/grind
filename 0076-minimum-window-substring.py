class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # counting the freq of t in a map
        freqT = Counter(t)

        # map for sliding window
        freqS = {}
        required = len(freqT.keys())
        have = 0
        window = (0, len(s))

        # sliding window
        l = 0
        for r in range(0, len(s)):
            # add letters to freqS if key exists in freqT
            if s[r] in freqT:
                freqS[s[r]] = freqS.get(s[r], 0) + 1

                # adjust have
                if freqS[s[r]] == freqT[s[r]]:
                    have += 1
            
            
                # adjust current window
                while have >= required:
                    # adjust output window
                    if r - l < window[1] - window[0]:
                        window = (l, r)
                    if s[l] in freqT:
                        freqS[s[l]] -= 1
                        if freqS[s[l]] < freqT[s[l]]:
                            have -= 1
                    l += 1
        
        if window == (0, len(s)):
            return ""
        else:
            return s[window[0] : window[1] + 1]


'''
time complexity O(n) where n == len(s) because we're doing constant operations for every single letter in s
space complexity O(1) because we can only have at most 52 different entries of key-value pairs for the 2 dictionaries (lowercase and uppercase english alphabets)
'''
