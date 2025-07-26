# https://leetcode.com/problems/merge-strings-alternately/

"""
・文字列をリストに変換するにはlist()を使用する
・リストを文字列に変換するには''.join()を使用する
・リストに要素を挿入するにはinsert()を使用する
  ※挿入のたびに後ろの要素をずらすためコストが高く、全体で二乗時間になりやすい
・リストの要素を取得するにはenumerate()を使用する
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_list = list(word1);
        for i, w2 in enumerate(word2):
            insert_index = i*2+1
            word_list.insert(insert_index, w2)
        output = ''.join(word_list)
        return output