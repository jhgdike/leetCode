class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda o: o[1])
        ans = 1
        left = points[0][1]
        for p in points:
            if p[0] > left:
                ans += 1
                left = p[1]
        return ans


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))
