class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        i = j = 0
        s = {(i, j)}
        for c in command:
            if c == 'R':
                i += 1
            else:
                j += 1
            s.add((i, j))

        def in_path(a, b):
            di, dj = a // i, b // j
            if (di > dj and (a - dj * i, b - dj * j) in s) or (di <= dj and (a - di * i, b - di * j) in s):
                return True
            return False
        if not in_path(x, y):
            return False
        for obs in obstacles:
            if obs[0] <= x and obs[1] <= y:
                if in_path(*obs):
                    return False
        return True




print(Solution().robot("URR",
[],
3,
2))
