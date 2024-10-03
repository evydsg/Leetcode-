class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        leftM = height[left]
        rightM = height[right]

        while left < right:
            if leftM < rightM:
                left += 1
                leftM = max(leftM, height[left])
                result += leftM - height[left]
            else:
                right -= 1
                rightM = max(rightM, height[right])
                result += rightM - height[right]
        
        return result