# https://leetcode.com/problems/length-of-last-word/

"""
知見：
・split()は、文字列を任意の文字で分割してリストにする
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst_length = tmp_length = 0
        for i, w in enumerate(s):
            if w == " ":
                if i >= 1 and s[i-1] != " ":
                    lst_length = tmp_length
                tmp_length = 0
            else:
                tmp_length += 1
        
        if tmp_length > 0:
            return tmp_length
        else:
            return lst_length

class CorrectSolution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        a=l[-1]
        return len(a)