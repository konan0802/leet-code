# https://leetcode.com/problems/can-place-flowers/

"""
解説：
・時間計算量: 両方とも O(n) - 配列を1回走査するため同じ
・空間計算量: 両方とも O(1) - 追加のデータ構造を使用せず

知見：
・判定を行う際は、基準値が変動した場合だけ判定を行うようにすると、速度が向上する
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True

        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empyt_right = (i == length-1) or (flowerbed[i+1] == 0)
                    
                if empty_left and empyt_right:
                    flowerbed[i] = 1
                    n -= 1
        
                    if n == 0:
                        return True

        return False


class CorrectSolution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
            
        for i, flower in enumerate(flowerbed):
            if flower == 0 and (
                i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1

                if n <= 0:
                    return True
        return False
