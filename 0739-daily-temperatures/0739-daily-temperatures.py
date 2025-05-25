class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time limit Exceeded : O(n^2)
        # ans=[0] *len(temperatures)
        # day_count=0
        # for i in range(len(temperatures)-1):
        #     for k in range(i, len(temperatures)):
        #         if temperatures[k]>temperatures[i]:
        #             day_count=len(temperatures[i:k])
        #             break
        #     ans[i]=day_count
        #     day_count=0
        # return(ans)

        ans = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                ans[stackInd] = (i - stackInd)
            stack.append([t, i])
        return(ans)

