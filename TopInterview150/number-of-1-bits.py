# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = format(n, '032b')

        count = 0
        for b in binary_str:
            if b == "1":
                count += 1
        
        return count