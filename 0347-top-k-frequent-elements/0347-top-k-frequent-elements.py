class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # step 1: list -> dict , increment value for count[num] for each occurence
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items(): # unpacking the dictionary
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): # right to left -> count
            for n in freq[i]: # for each entry in current count column
                res.append(n) # append entry
                if len(res) == k:
                    return res