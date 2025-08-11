# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_list = []
        for w in s:
            if w.isalpha() == True:
                s_list.append(w.lower())

        l = 0
        r = len(s_list)-1
        while l < r:
            if s_list[l] == s_list[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
            