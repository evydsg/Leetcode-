# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            Understand
                - The idea is to invert the tree

                Questions
                    - Can we have an empty tree?
            
            Match
                - Breadth-First Search Traversal

            Plan
                - Check if tree is empty
                    - Yes, return root
                - Initialize a queue
                - While queue is not empty
                    - Swap the current elements
                - Return the root

        """
        if root is None:
            return None
        
        queue = deque([root])
        
        while queue:
            current_node = queue.popleft()

            current_node.left, current_node.right = current_node.right, current_node.left

            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)
            
        return root
