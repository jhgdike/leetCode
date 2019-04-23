class Solution:
    def countPalindromicSubsequences(self, S):
        from collections import defaultdict
        import bisect
        M = 1000000007
        characters = defaultdict(list)
        for idx, s in enumerate(S):
            characters[s].append(idx)
        # print(characters)
        lookup = {}

        def helper(i, j):
            if i >= j: return 0
            if (i, j) in lookup:
                return lookup[(i, j)]
            res = 0
            for c, v in characters.items():
                # print(c, v)
                n = len(v)
                new_i = None
                idx_i = bisect.bisect_left(v, i)
                if idx_i < n:
                    new_i = v[idx_i]
                if new_i == None or new_i >= j:
                    continue
                idx_j = bisect.bisect_left(v, j) - 1
                new_j = v[idx_j]
                res += helper(new_i + 1, new_j) + 2 if new_i != new_j else 1
            lookup[(i, j)] = res % M
            # print(lookup)
            return lookup[(i, j)]

        return helper(0, len(S))


class Solution2(object):

    def countPalindromicSubsequences(self, s):
        m = int(1e9 + 7)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for ln in range(1, n + 1):
            for i in range(n - ln):
                j = i + ln
                if s[i] == s[j]:
                    left = i + 1
                    right = j - 1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                    if left > right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif left == right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                dp[i][j] = dp[i][j] + m if dp[i][j] < 0 else dp[i][j] % m
        return dp[0][n - 1]
