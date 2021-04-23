class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degree = [0] * n
        adj = [set() for _ in range(n)]
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
            in_degree[edge[0]] += 1
            in_degree[edge[1]] += 1
        queue = set()
        for i in range(n):
            if in_degree[i] == 1:
                queue.add(i)

        while queue:
            nlevel = set()
            for q in queue:
                for node in adj[q]:
                    in_degree[node] -= 1
                    if in_degree[node] == 1:
                        nlevel.add(node)
            if len(nlevel) == 0:
                return list(queue)
            queue = nlevel
        return [0]


# [1]
print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
# [3,4]
print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
# [0]
print(Solution().findMinHeightTrees(1, []))
# [0,1]
print(Solution().findMinHeightTrees(2, [[1,0]]))
# [1,2]
print(Solution().findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]))
