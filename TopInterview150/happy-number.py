# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            
            tmp = 0
            for nw in str(n):        
                tmp += int(nw)*int(nw)
            n = tmp
        
        return n == 1