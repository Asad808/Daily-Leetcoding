class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def toMinutes(timePoints):
            h, m = map(int, timePoints.split(":"))
            total_mins = (h * 60) + m
            return total_mins

        # total_min = toMinutes(timePoints)
        res = (1440 - toMinutes(timePoints[-1])) + toMinutes(timePoints[0])

        for i in range(len(timePoints)-1):
            # total_min = toMinutes(timePoints[])
            curr = toMinutes(timePoints[i+1])
            prev = toMinutes(timePoints[i])
            diff = curr - prev
            res = min(diff, res)

        return res