class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=deque()
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                ans.appendleft(nums[i])
            else:
                k+=1
        nums.clear()
        for j in range(len(ans)):
            nums.append(ans[j])
        print(k)