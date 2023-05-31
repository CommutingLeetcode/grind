class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()

        l, r = 0, len(s) - 1

        while l <= r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1

            if l < len(s) and r >= 0 and s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True


# two pointers, make sure to take care of edge case of char not alnum (another loop)
# Time complexity: O(n) as it's one iteration until l == r
# Space complexity: O(n) no data structure to store