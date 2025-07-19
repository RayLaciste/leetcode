class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [0] * len(nums)
        
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product = product * nums[j]

        #     res[i] = product
        
        # return res

        res = [0] * len(nums)
        before = [1] * len(nums)
        after = [1] * len(nums)

        for i in range(1, len(nums)):
            before[i] = nums[i - 1] * before[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            after[i] = nums[i + 1] * after[i + 1]
        
        for i in range(len(nums)):
            res[i] = before[i] * after[i]
        
        return res