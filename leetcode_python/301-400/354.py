class Solution(object):
    def winner(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda o: (o[0], -o[1]))

        # re_env = sorted(envelopes, key=lambda o: o[1])
        def lis(nums):
            res = []
            for n in nums:
                if len(res) == 0 or res[-1] < n:
                    res.append(n)
                else:
                    if res[-1] == n:
                        continue
                    for i in range(len(res)):
                        if res[i] >= n:
                            res[i] = n
                            break
            return res

        return len(lis([x[1] for x in envelopes]))

    def maxEnvelopes(self, envelopes):
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i + 1, len(envelopes)):
                if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


print(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3)  # 3
print(Solution().maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]) == 4)  # 4
print(Solution().maxEnvelopes(
    [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]) == 5)
