class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minDifference = 100

        def timeToMin(time):
            hour, minutes = map(int, time.split(":"))
            
            return (hour * 60) + minutes
        
        minDifference = 24 * 60 - timeToMin(timePoints[-1]) + timeToMin(timePoints[0])

        for index in range(len(timePoints)-1):
            previous = timeToMin(timePoints[index])
            current = timeToMin(timePoints[index + 1])

            minDifference = min(current - previous, minDifference)

            if minDifference == 0:
                return 0
        
        return minDifference
        