class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def helper(word):
            if word not in dic:
                bit = 0
                for w in word:
                    bit |= 1 << (ord(w) - ord('a'))
                dic[word] = bit

        res = 0
        dic = {}
        for i in range(len(words)):
            helper(words[i])
            for j in range(i, len(words)):
                helper(words[j])
                if not dic[words[i]] & dic[words[j]]:
                    res = max(res, len(words[j]) * len(words[i]))
        return res
