# https://leetcode.com/problems/isomorphic-strings/

"""
知見：
・zip(s, t)は、sとtの要素を同時に取り出す
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dist_kv = {}
        dist_vk = {}
        for i in range(len(s)):
            # キーが存在しており、値が異なる
            if s[i] in dist_kv and dist_kv[s[i]] != t[i]:
                return False
            
            # 値が存在しており、キーが異なる
            if t[i] in dist_vk and dist_vk[t[i]] != s[i]:
                return False

            # 追加            
            dist_kv[s[i]] = t[i]
            dist_vk[t[i]] = s[i]

        return True

class CorrectSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s2t = {}
        t2s = {}

        for a, b in zip(s, t):
            if a in s2t and s2t[a] != b:
                return False
            if b in t2s and t2s[b] != a:
                return False
            s2t[a] = b
            t2s[b] = a

        return True