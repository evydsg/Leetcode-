from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Understand
            - The idea is to return each level of the tree
        
            Question
                - Can we have an empty tree?

        Match
            - Breadth First Search Traversal

        Plan
            - Check if the tree is empty
                - Yes, return empty list
            - Initialize a list to store the result
            - Initialize a queue, and add root to the queue
            - While queue is not empty
                - Get the current size of the queue (number of nodes at the current level)
                - Initialize a list to store the current level's values
                - For each node at the current level:
                    - Pop the node from the queue
                    - Add the node's value to the current level list
                    - Append the node's left and right children to the queue (if they exist)
                - Append the current level list to the result list
            - Return the result list
        """
        
        if root is None:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            result.append(current_level)
        
        return result




