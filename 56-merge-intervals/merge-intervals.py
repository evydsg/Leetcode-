class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            Understand
                The idea is to merge all overlapping intervals

                Can we have an empty list?
                Are we always guaranteed to have overlapping intervals?
                Can we have duplicates in the interval?
            
            Match
                Two pointers
            
            Plan
                Initialize a list to keep track of the result
                Sort the list by using the first element


        """
        intervals.sort(key = lambda i:i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1] 

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        
        return result
        