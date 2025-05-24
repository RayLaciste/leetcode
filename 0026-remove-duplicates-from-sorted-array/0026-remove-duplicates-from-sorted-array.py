class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[0]*len(nums)
        my_set = list(sorted(set(nums)))
        for i in range(len(my_set)):
            nums[i] = my_set[i]
        return(len(my_set))