import collections
import heapq


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        a = collections.defaultdict(list)
        for f, t in tickets:
            heapq.heappush(a[f], t)
        stack = []

        def dfs(cur):
            while a[cur]:
                dfs(heapq.heappop(a[cur]))
            stack.append(cur)

        dfs("JFK")
        return stack[::-1]


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
