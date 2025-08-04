# https://leetcode.com/problems/spiral-matrix/

"""
・単純にシミュレーションを行ってしまうと複雑な状態管理＆条件分岐になる
・問題の構造化＆抽象化 ⇒ 不変条件の発見 ⇒ エッジケースの先読み
"""

class Solution:
    max_x = 0
    max_y = 0

    def judge(self, matrix: List[List[int]], xi: int, yi: int) -> bool:
        # 壁を越えない
        if xi > Solution.max_x or xi < 0 or yi > Solution.max_y or yi < 0:
            return False
        # 既に通った道を通らない
        if matrix[yi][xi] == "#":
            return False
        return True

    def add_direction(self, di: int) -> int:
        if di == 3:
            return 0
        return di + 1

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        Solution.max_x = len(matrix[0])-1
        Solution.max_y = len(matrix)-1
        directions = ["e","s","w","n"]

        output = []

        xi = 0
        yi = 0
        di = 0
        for i in range(len(matrix[0]) * len(matrix)):
            output.append(matrix[yi][xi])
            matrix[yi][xi] = "#"

            if directions[di] == "e":
                xi += 1

                # 方向転換
                if not self.judge(matrix, xi, yi):
                    xi -= 1
                    yi += 1
                    di = self.add_direction(di)
                    
                    # 方向転換後も阻まれたら
                    if not self.judge(matrix, xi, yi):
                        return output

            elif directions[di] == "s":
                yi += 1

                # 方向転換
                if not self.judge(matrix, xi, yi):
                    yi -= 1
                    xi -= 1
                    di = self.add_direction(di)
                    
                    # 方向転換後も阻まれたら
                    if not self.judge(matrix, xi, yi):
                        return output
                
            elif directions[di] == "w":
                xi -= 1

                # 方向転換
                if not self.judge(matrix, xi, yi):
                    xi += 1
                    yi -= 1
                    di = self.add_direction(di)
                    
                    # 方向転換後も阻まれたら
                    if not self.judge(matrix, xi, yi):
                        return output

            elif directions[di] == "n":
                yi -= 1

                # 方向転換
                if not self.judge(matrix, xi, yi):
                    yi += 1
                    xi += 1
                    di = self.add_direction(di)
                    
                    # 方向転換後も阻まれたら
                    if not self.judge(matrix, xi, yi):
                        return output


class CorrectSolution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        
        # 境界を設定
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # 右に移動 (上端の行)
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 下に移動 (右端の列)
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 左に移動 (下端の行) - 行が残っている場合のみ
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 上に移動 (左端の列) - 列が残っている場合のみ
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
    