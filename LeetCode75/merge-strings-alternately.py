# https://leetcode.com/problems/merge-strings-alternately/

"""
解説：
・Two-Pointerパターン：2つのポインタを使用して、2つの文字列を交互に結合する
・時間計算量：O(n) - 2つの文字列を1回ずつ走査
・空間計算量：O(1) - 追加のメモリ使用はなし

問題点：
・リストに要素を挿入するにはinsert()を使用する
  ※挿入のたびに後ろの要素をずらすためコストが高く、全体で二乗時間になりやすい

知見：
・文字列をリストに変換するにはlist()を使用する
・リストを文字列に変換するには''.join()を使用する
・リストの要素を取得するにはenumerate()を使用する
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_list = list(word1)
        for i, w2 in enumerate(word2):
            insert_index = i*2+1
            word_list.insert(insert_index, w2)
        output = ''.join(word_list)
        return output

class CorrectSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = j = 0
        
        # 両方の文字列に文字が残っている間、交互に追加
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        # 残りの文字を追加
        result.append(word1[i:])
        result.append(word2[j:])
        
        return ''.join(result)
