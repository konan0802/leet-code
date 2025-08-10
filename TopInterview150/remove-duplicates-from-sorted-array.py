# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
知見
・for num in nums: ではなく for i in range(len(nums)): でも良い
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        tmp = nums[0]
        for num in nums:
            if num > tmp:
                i += 1
                nums[i] = num
                tmp = num
        return i +1

class CorrectSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
            
        return k
        