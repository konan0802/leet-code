# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_indices = {}
        for i, n in enumerate(nums):
            if n in dict_indices and abs(i - dict_indices[n]) <= k:
                return True
            else:
                dict_indices[n] = i
        return False