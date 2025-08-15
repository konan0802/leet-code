# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    min_diff = None
    prev = None

    def defs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        self.defs(root.left)

        self.min_diff = min(self.min_diff, abs(self.prev - root.val))
        self.prev = root.val
        
        self.defs(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min_diff = 1000000
        self.prev = 1000000

        self.defs(root)
        return self.min_diff