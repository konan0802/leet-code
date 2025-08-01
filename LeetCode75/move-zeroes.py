# https://leetcode.com/problems/move-zeroes/

"""
解説：
・Two-Pointerパターン：「読み取り位置」と「書き込み位置」という2つの独立したポインタが協調して動作
・時間計算量：O(n) - 配列を最大2回走査
・空間計算量：O(1) - ポインタ変数jのみを使用し、追加配列は不要

問題点：
・zeros = [] で別の配列を作成し、空間計算量がO(k)になっている
・nums.pop() 操作は要素を削除する際に後続要素を前にシフトするため、1回の操作でO(n)の時間がかかる
・nums.extend() 操作はO(k)の時間がかかる
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        zeros = []
        while length > i:
            if nums[i] == 0:
                zeros.append(nums.pop(i))
                length-=1
            else:
                i += 1
        nums.extend(zeros)

class CorrectSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two-pointer approach: O(n) time, O(1) space
        """
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
