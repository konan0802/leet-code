# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        center = len(nums) // 2

        root = TreeNode(nums[center])

        nums_l = nums[:center]
        nums_r = nums[(center+1):]

        if len(nums_l):
            root.left = self.sortedArrayToBST(nums_l)
        if len(nums_r):
            root.right = self.sortedArrayToBST(nums_r)
         
        return root