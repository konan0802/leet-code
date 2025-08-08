# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
・再帰を利用する際には、分割統治のアプローチを考える
"""

class Solution:

    max_depth = 0

    def recursionDepth(self, root: Optional[TreeNode], depth: int) -> None:
        if root.left == None and root.right == None:
            self.max_depth = max(self.max_depth, depth)
        
        depth += 1

        if root.left:
            self.recursionDepth(root.left, depth)

        if root.right:
            self.recursionDepth(root.right, depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root:
            self.recursionDepth(root, 1)

        return self.max_depth


# 最適化された正解コード
class CorrectSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
