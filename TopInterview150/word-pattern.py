# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(' ')
        if len(pattern) != len(list_s):
            return False
        
        dict_p_s = {}
        dict_s_p = {}
        for pw, sw in zip(pattern, list_s):

            if pw in dict_p_s and dict_p_s[pw] != sw:
                return False
            if sw in dict_s_p and dict_s_p[sw] != pw:
                return False
            
            dict_p_s[pw] = sw
            dict_s_p[sw] = pw
        
        return True