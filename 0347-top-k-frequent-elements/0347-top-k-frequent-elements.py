class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = dict.fromkeys(nums, 0) # set values to 0
        ans = []

        for key in my_dict.keys(): # for each key
            for i in range(len(nums)):
                if key == nums[i]:
                    my_dict[key] += 1

        for i in range(k):
            res = sorted(my_dict, key=my_dict.get, reverse=True)[0]
            ans.append(res)
            my_dict.pop(res)

        return(ans)