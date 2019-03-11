from collections import Counter
from functools import reduce


def idx(a):
    return ord(a) - ord('a')


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = [0] * 26
        for a in A[0]:
            d[idx(a)] += 1

        for item in A[1:]:
            dd = [0] * 26
            for a in item:
                dd[idx(a)] += 1

            for i in range(26):
                d[i] = min(d[i], dd[i])
        res = []
        for i in range(26):
            if d[i]:
                res.extend([chr(i + 97)] * d[i])
        return res

    def s(self, A):
        a = Counter(A[0])
        for item in A[1:]:
            a &= Counter(item)
        return a.elements()

from collections import Counter
class Solution2(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())

        a = Counter(A[0])
        for item in A[1:]:
            a &= Counter(item)
        return list(a.elements())

print(Solution2().commonChars(["bella","label","roller"]))