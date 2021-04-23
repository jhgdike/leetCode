class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt = [0] * 10
        cntG = [0] * 10
        bull = cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                cnt[int(secret[i])] += 1
                cntG[int(guess[i])] += 1
        for i in range(10):
            cow += min(cnt[i], cntG[i])
        return str(bull) + 'A' + str(cow) + 'B'


print(Solution().getHint("1807", "7810"))
print(Solution().getHint("1123", "0111"))
