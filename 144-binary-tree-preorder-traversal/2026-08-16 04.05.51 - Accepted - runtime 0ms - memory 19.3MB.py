# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            #сначала в стек кидаем правого, чтобы левый оказался на вершине стека
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans