# https://leetcode.com/problems/greatest-common-divisor-of-strings/

"""
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
