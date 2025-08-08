class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def helper(i):
            if i >= n:
                return i == n
            
            if memo[i] != -1:
                return memo[i]
            else:
                memo[i] = helper(i + 1) + helper(i + 2)
                return memo[i]

        return helper(0)