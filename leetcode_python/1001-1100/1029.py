class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        for cost in costs:
            cost.append(abs(cost[0] - cost[1]))
        costs.sort(key=lambda o: o[2], reverse=True)
        N = len(costs) // 2
        a = b = 0
        total = 0
        for cost in costs:
            if a == N:
                total += cost[1]
                b += 1
            elif b == N:
                total += cost[0]
                a += 1
            else:
                if cost[0] < cost[1]:
                    a += 1
                    total += cost[0]
                else:
                    b += 1
                    total += cost[1]
        return total

    def solution2(self, costs):
        if not costs:
            return 0
        costs = sorted(costs, key=lambda cost: cost[1] - cost[0])
        res = 0
        lc = len(costs)
        for i in range(lc // 2):
            res += costs[i][1]
        for i in range(lc // 2, lc):
            res += costs[i][0]
        return res


print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
