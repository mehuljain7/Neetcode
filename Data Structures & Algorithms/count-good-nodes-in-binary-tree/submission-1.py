# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, curr, l):
        if not curr:
            return 0
        return int(curr.val >= l) + self.dfs(curr.left, max(curr.val, l)) + self.dfs(curr.right, max(curr.val, l))
    def goodNodes(self, root: TreeNode) -> int:
        l = float('-inf')
        return self.dfs(root, l)