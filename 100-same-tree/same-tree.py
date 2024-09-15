# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        queue1, queue2 = [p], [q]

        while queue1 and queue2:
            current1, current2 = queue1.pop(0), queue2.pop(0)

            if current1.val != current2.val:
                return False
            
            if current1.left and current2.left:
                queue1.append(current1.left)
                queue2.append(current2.left)
            elif current1.left or current2.left:
                return False
            if current1.right and current2.right:
                queue1.append(current1.right)
                queue2.append(current2.right)
            elif current1.right or current2.right:
                return False
        
        return True
