# https://leetcode.com/problems/is-subsequence/

"""
・Two Pointerを採用してもいいが、シンプルにfor文と、別のポインタを使う方がシンプル
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 文字列長
        s_len = len(s)
        t_len = len(t)

        # 例外
        if s_len > t_len:
            return False
        
        # Twoポインター
        si = 0
        ti = 0
        # sの文字列長に達するまで
        while s_len > si:
            if s[si] == t[ti]:
                si += 1
            ti += 1

            # tの残文字列長がc残文字列長を越えたら
            if s_len - si - 1 > t_len - ti - 1:
                return False

        return True


class CorrectSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False