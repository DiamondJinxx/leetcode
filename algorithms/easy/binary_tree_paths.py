from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs_path(root, prev_path):
            if not root:
                return 
            current_path = prev_path + '->' + str(root.val) if prev_path else str(root.val)
            if not root.left and not root.right:
                paths.append(current_path)
                return
            dfs_path(root.left, current_path)
            dfs_path(root.right, current_path)
        
        dfs_path(root, '')
        return paths
