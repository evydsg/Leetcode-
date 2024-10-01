# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth, queue = 0, [root]

        while queue:
            for level in range(len(queue)):
                current = queue.pop(0)

                if current:
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            
            depth += 1
        
        return depth