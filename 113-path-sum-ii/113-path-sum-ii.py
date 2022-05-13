# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, result, [], targetSum)
        return result
    
    def dfs(self, root, result, path, targetSum):
        if not root:
            return
        if not root.left and not root.right and root.val == targetSum:
            path.append(root.val)
            result.append(path)
        
        targetSum -= root.val
        
        self.dfs(root.left, result, path + [root.val], targetSum)
        self.dfs(root.right, result, path + [root.val], targetSum)