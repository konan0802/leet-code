# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_len = 0
        i = 0
        for num in nums:
            if num == val:
                val_len += 1
            else:
                nums[i] = num
                i += 1
        for _ in range(i, len(nums)):
            nums.pop(i)