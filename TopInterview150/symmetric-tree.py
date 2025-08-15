# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(r_left: Optional[TreeNode], r_right: Optional[TreeNode]) -> bool:
            if not r_left and not r_right:
                return True
            
            if not r_left or not r_right:
                return False
            
            if r_left.val != r_right.val:
                return False

            return isMirror(r_left.left, r_right.right) and isMirror(r_left.right, r_right.left)
            

        if not root:
            return True
        
        return isMirror(root.left, root.right)