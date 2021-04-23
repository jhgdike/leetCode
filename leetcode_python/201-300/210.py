class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if len(prerequisites) == 0:
            return range(numCourses)
        in_degrees = [0] * numCourses
        adj = [set() for _ in range(numCourses)]
        for p in prerequisites:
            adj[p[1]].add(p[0])
            in_degrees[p[0]] += 1
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        res = []
        while queue:
            top = queue.pop()
            res.append(top)
            for a in adj[top]:
                in_degrees[a] -= 1
                if in_degrees[a] == 0:
                    queue.append(a)
        if len(res) < numCourses:
            return []
        return res


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2, [[1,0]]))
