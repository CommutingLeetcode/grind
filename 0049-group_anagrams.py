class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = [0] * 26
            for i in word:
                count[ord(i) - ord("a")] += 1

            # groupkeys = (1,0,0,0,1,.....,0)
            groupkey = tuple(count)

            # we want to initialize the dictionary to map tuples to an array
            if groupkey not in group:
                group[groupkey] = [word]
            else:
                group[groupkey].append(word)

        return group.values()
        group = {}
    
        return group.values()
            

### NOTES
# The key for this problem is to count the number of occurences of each alphabets
# in the word. After getting the occurences (count), we then need to map it to 
# all the previous words in a dictionary. Ex: aet->[eat,ate].
# Since we are iterating through the array once (n), thenn each of the letters in 
# the word (avg. of m) so the complexity will be O(mn)

### FYI
# we can use ord() to find the ASCII value of a character
# keys of dictionaries must be immutable -> so we are using tuples
