class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lolw = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] is ' ' and lolw is not 0:
                return lolw
            if s[i] is not ' ':
                lolw += 1

        return lolw

### NOTES
# Iterate the string from the back and stopping
# when whitespace is found. Take into account the
# string having whitespace at the back
