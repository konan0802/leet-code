# https://leetcode.com/problems/n-th-tribonacci-number/

"""
・メモ化再帰は、再帰関数の結果をキャッシュすることで、同じ計算を繰り返さないようにする
"""

class Solution:
    
    cache = {0:0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return self.cache[n]
        else:
            self.cache[n-1] = self.tribonacci(n-1)
            return self.cache[n-1] + self.cache[n-2] + self.cache[n-3]