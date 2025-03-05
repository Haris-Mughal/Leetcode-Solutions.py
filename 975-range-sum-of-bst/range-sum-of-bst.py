# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        leftTree = self.rangeSumBST(root.left, low, high)
        rightTree = self.rangeSumBST(root.right, low, high)
    
        if root.val > high:
            return leftTree
    
        if root.val < low:
            return rightTree
    
        return (root.val + rightTree + leftTree)