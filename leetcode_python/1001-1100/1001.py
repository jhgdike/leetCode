class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dict_x, dict_y, dict_d1, dict_d2, res = {}, {}, {}, {}, []
        set_lamps = set()
        for x, y in lamps:
            if (x, y) in set_lamps:
                continue
            dict_x[x] = dict_x.get(x, 0) + 1
            dict_y[y] = dict_y.get(y, 0) + 1
            dict_d1[x + y] = dict_d1.get(x + y, 0) + 1
            dict_d2[x - y] = dict_d2.get(x - y, 0) + 1
            set_lamps.add((x, y))
        res = []
        for x, y in queries:
            if dict_x.get(x) or dict_y.get(y) or dict_d1.get(x+y) or dict_d2.get(x-y):
                res.append(1)
            else:
                res.append(0)
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    loc_x, loc_y = x + i, y + j
                    if (loc_x, loc_y) in set_lamps:
                        dict_x[loc_x] -= 1
                        dict_y[loc_y] -= 1
                        dict_d1[loc_x + loc_y] -= 1
                        dict_d2[loc_x - loc_y] -= 1
                        set_lamps.remove((loc_x, loc_y))
        return res


"""
 Swift LeetCode https://github.com/strengthen/LeetCode

Swift LeetCode 目录 | Catalog https://www.cnblogs.com/strengthen/p/9895524.html

LeetCode997. 找到小镇的法官 | Find the Town Judge https://www.cnblogs.com/strengthen/p/10429029.html

LeetCode998. 最大二叉树 II | Maximum Binary Tree II https://www.cnblogs.com/strengthen/p/10429077.html

LeetCode999. 车的可用捕获量 | Available Captures for Rook https://www.cnblogs.com/strengthen/p/10429051.html

LeetCode1001. 网格照明 | Grid Illumination https://www.cnblogs.com/strengthen/p/10430537.html
"""
