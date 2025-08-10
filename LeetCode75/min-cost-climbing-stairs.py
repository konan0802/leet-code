# https://leetcode.com/problems/min-cost-climbing-stairs/

"""
・問題の構造を自然に表現する順方向のアプローチが一般的により好ましい
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0]*n

        for i in range(n-1, -1, -1):
            if i >= n-2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])

class CorrectSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i - 2])
        return dp[n]
