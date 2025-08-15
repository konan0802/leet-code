# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        res = ""
        for w in str_x:
            res = w + res
        return str_x == res