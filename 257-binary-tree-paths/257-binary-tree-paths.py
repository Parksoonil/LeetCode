# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        self.dfs(root, "", result)
        return result
    def dfs(self, root, ls, result):
        if not root.left and not root.right:
            result.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + "->", result)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + "->", result)