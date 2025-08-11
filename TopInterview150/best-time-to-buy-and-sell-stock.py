# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
知見：
・diffsに全てを格納せずとも、最大値だけ保持しておけば良い
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        c_min = prices[0]
        c_max = prices[0]
        diffs = []

        for price in prices:
            c_max = max(c_max, price)

            if price < c_min:
                diffs.append(c_max - c_min)
                c_min, c_max = price, price
        
        if len(diffs) == 0:
            return (c_max - c_min)
        
        return max(max(diffs), (c_max - c_min))


class CorrectSolution:
    def maxProfit(self, prices: List[int]) -> int:
        
        c_min = prices[0]
        c_max = prices[0]
        diff = 0

        for price in prices:

            # 最大値を更新
            if price > c_max:
                c_max = price
                diff = max(diff, (c_max - c_min))

            # 最小値を更新（最大値も更新）
            if price < c_min:
                c_min, c_max = price, price
        
        return diff