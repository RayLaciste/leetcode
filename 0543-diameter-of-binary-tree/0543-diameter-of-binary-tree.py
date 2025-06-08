# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # setting a `global` variable

        def dfs(curr): # returns height
            if curr is None:
                return 0
            
            left = dfs(curr.left) # gets height of left
            right = dfs(curr.right) # gets height of right

            self.ans = max(self.ans, left + right) # ans updates to biggest
            return 1 + max(left, right) # return the height from the current node for earlier recursive calls
        
        dfs(root)
        return self.ans