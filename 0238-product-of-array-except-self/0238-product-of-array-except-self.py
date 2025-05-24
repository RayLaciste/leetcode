class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1] * len(nums) # initialize answer list        
        
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
            """
            [1, 2, 4, 6] -> ans[1,1,2,8]
            """
        #postfix
        postfix=1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return(ans)