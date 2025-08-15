# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = '{:032b}'.format(n)
        reversed_str = binary_str[::-1]
        return int(reversed_str, 2)
