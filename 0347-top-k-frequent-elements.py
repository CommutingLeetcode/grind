class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        nums2d = [[] for _ in range(len(nums) + 1)]
        # 2-d arr index from 0 to len(nums) inclusive

        for num, count in counter.items():
            nums2d[count].append(num)

        res = []

        for i in range(len(nums2d) - 1, -1, -1):
            for num in nums2d[i]:
                res.append(num)
                if len(res) == k:
                    return res

# use Counter (hashset for nums, count)
# use 2d array where index is frequency and arr[index] is the nums with that freq
# have result as empty array
# iterate backwards (from most freq) and fill res until len(res) == k

# Time Complexity: O(n), n == len(nums)