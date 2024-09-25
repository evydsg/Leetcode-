class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        sIndex, eIndex = 0, 0
        result, count = 0, 0

        while sIndex < len(intervals):
            if start[sIndex] < end[eIndex]:
                sIndex += 1
                count += 1
            else:
                eIndex += 1
                count -= 1
            
            result = max(result, count)
        
        return result