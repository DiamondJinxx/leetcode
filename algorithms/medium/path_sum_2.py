from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs_path(root, prev_path, prev_sum=0):
            if not root:
                return
            current_sum = prev_sum + root.val
            prev_path.append(root.val)
            if not root.left and not root.right and current_sum == targetSum:
                paths.append(prev_path.copy())
            dfs_path(root.left, prev_path.copy(), current_sum)
            dfs_path(root.right, prev_path.copy(), current_sum)
        
        dfs_path(root, [])

        return paths
