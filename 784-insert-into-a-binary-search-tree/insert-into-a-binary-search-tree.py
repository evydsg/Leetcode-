# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    Understand: add a value to the tree assuming that the value is not yet there
        - First, find out the perfect location to insert the tree
        - Second, create a new node

        - Can the three be empty?
        - Can the value be negative?

    Match
        BST Search
    
    Plan (Iteratively)
        - Check if the tree is empty
            - Create new Node
        - Initialize a pointer to start from the root
        - Iterate through the tree as long as current has a value
            - Check if the value is less or greater than root
                - Check if root has a value on one of the branches
                    - No, create a new node
                    - Yes, assign the next node to the next subtree
        - Return root

"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        current = root

        while current:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
        
        return root
        