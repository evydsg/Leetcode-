# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            Understand
                - The idea of the exercise is to check if two trees are the same
                
                Questions
                    - Can we have empty lists?
            
            Match
                - Binary Tree Traversal
            
            Plan
                - Check if any of the roots if empty
                - Traverse through the tree
                    - Check if the current value of the nodes are the same
                        - No, return false
            
            Evaluate
                - Time Complexity: O(n)
                - Space Complexity: O(n)

        """

        if p is None and q is None:
            return True
        
        if p is None:
            return False
            
        if q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)