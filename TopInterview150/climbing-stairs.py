# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 2
            else:
                dp[i] += dp[i-1]
                dp[i] += dp[i-2]
        return dp[n-1]