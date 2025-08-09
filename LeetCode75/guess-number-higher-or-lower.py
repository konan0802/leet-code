# https://leetcode.com/problems/guess-number-higher-or-lower/

"""
・二分探索は、再帰ではなく、while文で実装することにより、よりシンプルに実装できる
・再帰による無駄なオーバーヘッドを削減できる
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.dfs(0, n, n)

    def dfs(self, m: int, n: int, c:int) -> int:
        g = guess(c)
        if g == 0:
            return c
        elif g == -1:
            return self.dfs(m, c, (m+c)//2)
        else:
            return self.dfs(c, n, (c+n)//2)


class CorrectSolution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1  # Should never reach here