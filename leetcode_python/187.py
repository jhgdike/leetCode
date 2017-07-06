class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        string = {}
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] not in string:
                string[s[i:i + 10]] = 1
            else:
                if string[s[i:i+10]] == 1:
                    res.append(s[i:i+10])
                string[s[i:i + 10]] += 1
        return res
