# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur: # while current is not none
            if p.val > cur.val and q.val > cur.val: #  p and q are not in left sub tree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: # p and q are not in right sub tree
                cur = cur.left
            else: # p is in left sub tree, q is in right sub tree
                return cur
