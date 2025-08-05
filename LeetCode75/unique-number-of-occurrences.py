# https://leetcode.com/problems/unique-number-of-occurrences/

"""
知見
・values()を用いることで、辞書の値を取得できる
・setを用いることで、重複を削除できる
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for a in arr:
            if a not in hash_map:
                hash_map[a] = 1
            else:
                hash_map[a] += 1

        return len(hash_map.values()) == len(set(hash_map.values()))
