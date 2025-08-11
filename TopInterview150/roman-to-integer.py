# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dist = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for i, w in enumerate(s):
            
            # I can be placed before V and X to make 4 and 9. 
            if w in ("V", "X") and i >= 1 and s[i-1] == "I":
                result += (roman_dist[w] - 2)
            
            # X can be placed before L and C to make 40 and 90. 
            elif w in ("L", "C") and i >= 1 and s[i-1] == "X":
                result += (roman_dist[w] - 20)
            
            # C can be placed before D and M to make 400 and 900.
            elif w in ("D", "M") and i >= 1 and s[i-1] == "C":
                result += (roman_dist[w] - 200)
            
            else:
                result += roman_dist[w]

        return result