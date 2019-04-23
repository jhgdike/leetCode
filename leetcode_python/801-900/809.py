class Solution(object):

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        s_list = []
        c_list = []
        i = 0
        while i < len(S):
            cur = S[i]
            repeat = 1
            while i + 1 < len(S) and S[i] == S[i+1]:
                repeat += 1
                i += 1
            s_list.append(cur)
            c_list.append(repeat)
            i += 1

        for word in words:
            if self.com(s_list, c_list, word):
                res += 1
        return res

    def com(self, s_list, c_list, word):
        k = 0
        for i in range(len(s_list)):
            if k >= len(word):
                return False
            s = s_list[i]
            c = c_list[i]
            if word[k] != s:
                return False
            repeat = 1
            while k + 1 < len(word) and word[k] == word[k+1]:
                repeat += 1
                k += 1
            if repeat > c or (c == 2 and repeat == 1):
                return False
            k += 1
        return True


S = "heeelllooo"
words = ["hello", "hi", "hellllo"]

Solution().expressiveWords(S, words)
