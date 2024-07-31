class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                print(f'i: {i}')
                print(f'j: {j}')
                print(f'check if {s[i:j+1]} is palindrome')
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    print(f'part after appending: {part}')
                    dfs(j + 1)
                    part.pop()
                    print(f'part after popping: {part}')

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

'''
might be the hardest leetcode question I've done so far. Took me around 2 hours to understand and I still don't fully understand it.
time complexity is 2^n * n. 2^n because we can choose to either partition or not partition between each characters. n because there are n letters. (see i can't even explain it that properly)

'''
