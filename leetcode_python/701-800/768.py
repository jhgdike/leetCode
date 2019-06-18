class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        d = dict()
        for i, s in enumerate(S):
            d[s] = i
        cur = 0
        while cur < len(S):
            nx = self.find_first_word(S, d, cur)
            ans.append(nx-cur+1)
            cur = nx + 1
        return ans

    def find_first_word(self, S, d, left):
        right = d[S[left]]
        for i in range(left + 1, len(S)):
            if i >= right:
                break
            right = max(right, d[S[i]])
        return right


class Solution2(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        while S:
            cur = self.find_first_word(S)
            S = S[cur+1:]
            ans.append(cur+1)
        return ans

    def find_first_word(self, S):
        left, right = 1, 0
        for i in range(len(S) - 1, 0, -1):
            if S[i] == S[0]:
                right = i
                break
        if right == 0:
            return right
        while left < right:
            for i in range(len(S) - 1, right, -1):
                if S[i] == S[left]:
                    right = i
                    break
            left += 1
        return right


S = "qvmwtmzzse"
print(Solution().partitionLabels(S))
