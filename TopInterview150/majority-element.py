# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        summary = {}
        for num in nums:
            if num in summary:
                summary[num] += 1
            else:
                summary[num] = 1
        
        return max(summary, key=summary.get)
