# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) > len(b):
            alpha = a
            beta = b
        else:
            alpha = b
            beta = a

        max_l = len(alpha)
        diff_l = len(alpha) - len(beta)

        beta = diff_l * "0" + beta
        
        res = ""
        kuriage = 0
        for i in range(-1, (max_l*-1)-1, -1):
            total = int(alpha[i]) + int(beta[i]) + kuriage
            if total == 3:
                res = "1" + res
                kuriage = 1
            elif total == 2:
                res = "0" + res
                kuriage = 1
            elif total == 1:
                res = "1" + res
                kuriage = 0
            else:
                res = "0" + res
                kuriage = 0
        
        if kuriage == 1:
            res = "1" + res

        return res