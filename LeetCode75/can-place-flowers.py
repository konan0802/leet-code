# https://leetcode.com/problems/can-place-flowers/

"""
・判定を行う際は、基準値が変動した場合だけ判定を行うようにすると、速度が向上する
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True;

        length = len(flowerbed);
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0);
                empyt_right = (i == length-1) or (flowerbed[i+1] == 0);
                    
                if empty_left and empyt_right:
                    flowerbed[i] = 1;
                    n -= 1;
        
                    if n == 0:
                        return True;

        return False;
