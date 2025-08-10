# https://leetcode.com/problems/single-number/

"""
Single Number問題の解法

問題: 配列内で1つだけ1回出現し、他は2回出現する数を見つける
制約: 時間O(n), 空間O(1)

解法: XOR演算の性質を活用
- a ^ a = 0 (同じ数は消える)
- a ^ 0 = a (0は影響しない)
- XORは交換・結合法則が成り立つ
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
