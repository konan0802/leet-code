# https://leetcode.com/problems/ransom-note/

"""
知見：
・自身で実装可能なレベルのライブラリは使わない
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        dist = {}
        for m in magazine:
            if m in dist:
                dist[m] += 1
            else:
                dist[m] = 1
        
        for r in ransomNote:
            if r not in dist or dist[r] == 0:
                return False
            dist[r] -= 1
        
        return True

class CorrectSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for s in ransomNote:
            if s not in magazine:
                return False
            magazine = magazine.replace(s, '', 1)
        return True

        