# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return 1

        # seq_length=1
        # max_length=1
        # s_nums = sorted(set(nums))
        # print(s_nums)
        # for i in range(len(s_nums)-1):
        #     if s_nums[i] + 1 == s_nums[i+1]:
        #         seq_length+=1
        #     else:
        #         if seq_length>max_length:
        #             max_length=seq_length
        #         seq_length=1
        #     if seq_length>max_length:
        #             max_length=seq_length
        # return max_length
        # ^ My original solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1    
                longest = max(longest, length)
        return longest