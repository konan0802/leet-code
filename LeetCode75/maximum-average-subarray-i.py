# https://leetcode.com/problems/maximum-average-subarray-i/

"""
解説
・スライディングウィンドウの問題
・時間計算量：O(n)
・空間計算量：O(1)

知見
・初期値（current_sum）の置き方を工夫する
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
