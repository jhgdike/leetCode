class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in strs:
            tmp = [0] * 26
            for c in item:
                tmp[ord(c)-ord('a')] += 1
            key = '-'.join(map(str, tmp))
            dic.setdefault(key, [])
            dic[key].append(item)
        return dic.values()
