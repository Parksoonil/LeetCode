# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []
        self.dfs(root, result)
        first, second = None, None
        for i in range(len(result) - 1):
            if result[i].val > result[i + 1].val and not first:
                first = result[i]
            if result[i].val > result[i + 1].val and first:
                second = result[i + 1]
        first.val, second.val = second.val, first.val
    def dfs(self, root, result):
        if root:
            self.dfs(root.left, result)
            result.append(root)
            self.dfs(root.right, result)
            
    