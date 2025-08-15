# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = -1
        right = len(nums)

        while left+1 < right:
            center = (left+right)//2
            print("center:{}, left:{}, right:{}".format(center,left,right))
            if target > nums[center]:
                left = center
            else:
                right = center
        
        return center if target==nums[center] else right