# 452 - Minimum number of arrows to burst balloons

class Solution:
    def findMinArrowShots(self, points):
        # sort arr with respect to end pos of balloon
        points = sorted(points, key=lambda x:x[1])

        # get first endpoint of points
        end = points[0][1]

        arrow = 1

        for i in range(1, len(points)):
            if points[i][0] <= end: continue

            else:
                end = points[i][1]
                arrow = arrow + 1

        return arrow
        


points = [[10,16],[2,8],[1,6],[7,12]]
print(Solution().findMinArrowShots(points))

points = [[1,2],[3,4],[5,6],[7,8]]
print(Solution().findMinArrowShots(points))

points = [[1,2],[2,3],[3,4],[4,5]]
print(Solution().findMinArrowShots(points))
