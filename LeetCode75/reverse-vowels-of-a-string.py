# https://leetcode.com/problems/reverse-vowels-of-a-string/

"""
・双方向ポインタ（two-pointer）アプローチで効率的に解決
・1回のループで母音を交換し、追加の配列も不要
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s)-1
        s = list(s)

        while left <= right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1

        return ''.join(s)