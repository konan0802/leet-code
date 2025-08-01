# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

"""
解説：
・リスト内包表記はPythonのC言語レベルで最適化されているため、実際の実行時間は最適化版の方が約20-30%高速
・時間計算量: O(n) - リストの最大値を求めるために1回のループ
・空間計算量: O(n) - 結果のリストを作成するために1回のループ
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxBefore = max(candies)
        result = list()
        for i, n in enumerate(candies):
            if n + extraCandies >= maxBefore:
                result.append(True)
            else:
                result.append(False)
        return result


class CorrectSolution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]