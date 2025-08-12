# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dist_s = {}
        dist_t = {}
        for sw, tw in zip(s,t):
            if sw in dist_s:
                dist_s[sw] += 1
            else:
                dist_s[sw] = 1
            
            if tw in dist_t:
                dist_t[tw] += 1
            else:
                dist_t[tw] = 1
            
        
        for sw in dist_s:
            if sw not in dist_t or dist_s[sw] != dist_t[sw]:
                return False
        
        return True

