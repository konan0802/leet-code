# https://leetcode.com/problems/greatest-common-divisor-of-strings/

"""
解説：
・時間計算量: O(m + n) - 文字列連結とGCD計算
・空間計算量: O(m + n) - 文字列連結のための一時的なスペース

知見：
・ライブラリの読み込み時には利用するものだけを読み込む
・`Brute force`ではなく、必ず数学的アプローチを利用する
"""

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]

class CorrectSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        最適化された解法 - 数学的アプローチ
        
        キーアイデア:
        1. 共通除数が存在する条件: str1 + str2 == str2 + str1
        2. 最大共通除数の長さ: gcd(len(str1), len(str2))
        3. 結果: str1の最初のgcd_len文字
        
        時間計算量: O(m + n) - 文字列連結とGCD計算
        空間計算量: O(m + n) - 文字列連結のための一時的なスペース
        """
        # 共通除数が存在するかチェック
        # もし存在するなら、str1 + str2 == str2 + str1が成り立つ
        if str1 + str2 != str2 + str1:
            return ""
        
        # 両文字列の長さの最大公約数を計算
        # これが最大共通除数文字列の長さになる
        gcd_len = gcd(len(str1), len(str2))
        
        # str1の最初のgcd_len文字が答え
        return str1[:gcd_len]
