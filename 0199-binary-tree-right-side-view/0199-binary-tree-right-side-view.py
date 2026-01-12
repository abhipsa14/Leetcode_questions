# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        level=0
        def rev(node,level,ans):
            if node is None:
                return
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                rev(node.right,level+1,ans)
            if node.left:
                rev(node.left,level+1,ans)
        rev(root,level,ans)
        return ans
            
