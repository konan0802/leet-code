# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, w in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != w:
                    return prefix
            prefix += w
        return prefix