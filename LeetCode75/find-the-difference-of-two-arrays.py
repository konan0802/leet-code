# https://leetcode.com/problems/find-the-difference-of-two-arrays/

"""
解説
・setを用いることで、重複を削除する

知見
・変数定義を1行で行うことで、コードを簡潔にする
・リスト内包表記を用いることで、1行で計算できる
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer = []
        answer.append(list(set1-set2))
        answer.append(list(set2-set1))
        
        return answer

# 最適化されたCorrectSolutionクラス
class CorrectSolution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 1行で計算、set演算を直接リスト内包表記で実行
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
