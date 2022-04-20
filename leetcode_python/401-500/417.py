from queue import deque


class Solution:
    def pacificAtlantic(self, heights):
        deq = set()
        for i in range(len(heights[0])):
            deq.add((0, i))
        for i in range(1, len(heights)):
            deq.add((i, 0))

        end1 = set()

        def ok(q, point):
            for item in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = point[0] + item[0], point[1] + item[1]
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]) and heights[x][y] >= 0 and heights[x][y] >= heights[point[0]][point[1]]:
                    q.add((x, y))

        while deq:
            point = deq.pop()
            if point not in end1:
                end1.add(point)
                ok(deq, point)

        deq2 = set()
        end2 = set()
        for i in range(len(heights[0])):
            deq2.add((len(heights) - 1, i))
        for i in range(len(heights) - 1):
            deq2.add((i, len(heights[0]) - 1))

        while deq2:
            point = deq2.pop()
            if point not in end2:
                end2.add(point)
                ok(deq2, point)
        return [list(x) for x in end1 & end2]


print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
