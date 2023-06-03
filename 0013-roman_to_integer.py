## reverse string solution
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
        
#         # The logic is that IX is a special case since I is smaller than X
#         # but it is on X's left. When we see a number that gets smaller,
#         # we can substract it instead of adding it. For this to work, wee
#         # need to iterate backwards

#         sum = 0
#         prev_num = 'I'  #no numeral is smaller than I

#         for i in s[::-1]:   #iterate backwards
#             if roman[i] < roman[prev_num]:
#                 sum -= roman[i]
#             else:
#                 sum += roman[i]
#             prev_num = i

#         return sum

## Double dictionary solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        convert = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC",
        }

        for k,v in convert.items(): #replace IV with VIIII, etc.
            s = s.replace(k,v)

        sum = 0
        for i in range(0, len(s)):
            sum += roman[s[i]]

        return sum