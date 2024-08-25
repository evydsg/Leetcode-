class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            Understand
                The idea is to find the two bars that form the maximum container

                Edge cases

                Questions
                    Can we have an empty array?
                    Can we have duplicates?
                    Can we find negative integers in the array?

            Match
                Two pointers
                    One starting from the end and the other from the start

            Plan
                Initialize a variable to keep track of the maxArea
                Initialize two pointers
                    left
                    right
                Iterate through the array
                Find the minimum between height minimum and right
                If left is less than right, incremenet
                If right is less than left, decrement
                Update the maxArea

            Evaluate
                Time complexity: O(n)
                Space complexity: O(1)
        """
        maxWater = 0
        left, right = 0, len(heights)-1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -= 1
                left += 1

        return maxWater