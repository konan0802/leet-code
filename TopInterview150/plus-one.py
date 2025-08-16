# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_int = str(int(''.join(map(str, digits)))+1)
        return [int(n) for n in list(digits_int)]