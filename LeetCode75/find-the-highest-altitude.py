# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitudes = 0
        max_altitudes = 0
        for p in gain:
            current_altitudes += p
            max_altitudes = max(max_altitudes, current_altitudes)
        return max_altitudes