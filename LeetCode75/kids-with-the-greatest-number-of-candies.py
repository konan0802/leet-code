# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

"""
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxBefore = max(candies);
        result = list();
        for i, n in enumerate(candies):
            if n + extraCandies >= maxBefore:
                result.append(True);
            else:
                result.append(False);
        return result;