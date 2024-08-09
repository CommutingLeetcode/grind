class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        output = ""
        for str in strs:
            length = len(str)
            output += f"{length}#{str}"
        return output

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        i = 0
        output = []
        while i < len(str):
            # get the length of the word
            j = i
            while str[j] != "#":
                j += 1           
            length = int(str[i : j])
            output.append(str[j+1 : j+length+1])
            i = j + length + 1
        return output
'''
good solution, basically iterating using a variable interval. having a second inner while loop to process the length of the string first, then updating i to the start of the new entry. Need to understand string slicing very well here
O(n) time complexity and O(1) space complexity
'''
