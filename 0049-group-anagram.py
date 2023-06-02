class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return res.values()

# make a collections that can take a 26-sized tuple  as its index
# then basically just make the char counter of each string and append it into the index (2-d array)
# then just return the values of that (index, values) pair

# Time Complexity: O(mn) where m is len(strs) and n is max of len(s) in strs