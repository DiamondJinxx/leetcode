from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BHS
        queue = deque([p, q])

        while queue:
            left, right = queue.popleft(), queue.popleft()

            if not left and not right:
                continue

            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.extend([left.left, right.left, left.right, right.right])

        return True


    # dfs
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
            # return True
        # if not p or not q:
            # return False
        # if p.val != q.val:
            # return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
