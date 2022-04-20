class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        ans = 0
        lines = input.split('\n')
        path = []
        for line in lines:
            c = line.count('\t')
            if c == len(path):
                path.append(line[c:])
            else:
                path = path[:c]
                path.append(line[c:])
            if '.' in path[-1]:
                cur = 0
                for v in path:
                    cur += len(v)
                cur += len(path)-1
                if cur > ans:
                    ans = cur
        return ans
