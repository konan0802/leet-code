# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        if len(nums) == 0:
            return res
        
        tmp_start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if tmp_start == nums[i-1]:
                    res.append("{}".format(tmp_start))
                else:
                    res.append("{}->{}".format(tmp_start, nums[i-1]))
                tmp_start = nums[i]
        
        if tmp_start == nums[-1]:
                res.append("{}".format(tmp_start))
        else:
            res.append("{}->{}".format(tmp_start, nums[-1]))
        
        return res