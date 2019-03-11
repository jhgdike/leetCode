class Solution(object):
    def longestOnes(self, A, K):

        k = K
        index_zero = []
        pop = 0
        dp = [0] * len(A)
        if A[0] == 0 and k > 0:
            dp[0] = 1
            k -= 1
            index_zero.append(0)
        else:
            dp[0] = A[0]
        for i in range(1, len(A)):
            if A[i] == 0:
                index_zero.append(i)
                if k > 0:
                    dp[i] = dp[i-1] + 1
                    k -= 1
                else:
                    if len(index_zero) > K:
                        pop = index_zero.pop(0)
                    dp[i] = len(A[pop+1:i+1])
            else:
                dp[i] = dp[i-1] + 1
        return dp[-1]
