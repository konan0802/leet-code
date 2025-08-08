# https://leetcode.com/problems/leaf-similar-trees/

"""
・yieldを用いると、再帰関数の結果をリストに変換せずに、そのまま返すことができる
"""

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def recursion(root: Optional[TreeNode]) -> List:
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [root.val]
            return recursion(root.left) + recursion(root.right)
        
        return recursion(root1) == recursion(root2)


class CorrectSolution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        
        return list(dfs(root1)) == list(dfs(root2))