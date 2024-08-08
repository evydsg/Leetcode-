# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            Understand
                - The idea is to check if the binary tree is valid. A valid binary tree is left < root < right

                Questions
                    - Can we have an empty tree?
                    - What kind of elements are we supposed to receive?
            
            Match
                - Inorder traversal

            
            Plan
                - Check if root is None
                - Define a function to help traverse through the tree
                - Check if the current value is less than the current value for the left
                - Check if current value is greater than the current value for the right

            Evaluate
                - Time Complexity: O(h) for the height of the tree
                - Space Complexity: O()

        """
        if root is None:
            return True
        
        stack = []

        prevNode = None
        node = root #2

        while stack or node:
            while node: #node still has a value
                stack.append(node) #stack = [2]
                node = node.left # node = 1
            
            node = stack.pop() #node = 2

            if prevNode is not None and node.val <= prevNode: 
                return False
            
            prevNode = node.val
        
            node = node.right

        return True
            

        