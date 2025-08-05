# https://leetcode.com/problems/find-pivot-index/

"""
・方針（Prefix Sum）は正しいが、数学的に考えると簡略化できる部分が存在した
  ・具体的には双方向Prefix Sumを用いたが、片方のPrefix Sumを用いるだけで良い
  ・その場合は、total_sum - nums[i] == 2 * left_sum で判定できる
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        li = 0
        ri = n-1

        l_total = [0]*n
        r_total = [0]*n

        l_current = 0
        r_current = 0

        for _ in range(n):
            # 左からの合計
            l_current += nums[li]
            l_total[li] = l_current
            li += 1

            # 右からの合計
            r_current += nums[ri]
            r_total[ri] = r_current
            ri -= 1

        for i in range(n):
            if l_total[i] == r_total[i]:
                return i
        return -1


class CorrectSolution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # right_sum = total_sum - left_sum - nums[i]
            # if left_sum == right_sum, then total_sum - nums[i] == 2 * left_sum
            if total_sum - nums[i] == 2 * left_sum:
                return i
            left_sum += nums[i]
        
        return -1