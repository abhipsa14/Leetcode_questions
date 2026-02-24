# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def solve(root,val):
            if not root:
                return 0
            val=(2*val)+1*root.val
            if not root.left and not root.right:
                return val
            return solve(root.left,val)+solve(root.right,val)
        return solve(root,0)
        