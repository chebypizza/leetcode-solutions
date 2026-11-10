# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        ar = []

        while queue:
            levelSize = len(queue) 
            currentLevel = []
            for _ in range(levelSize):
                cur = queue.popleft()

                currentLevel.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ar.append(currentLevel)

        return ar