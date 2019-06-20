class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        da = dict()
        length = len(tasks)
        for t in tasks:
            da[t] = da.get(t, 0) + 1
        tasks = list(da.values())
        tasks.sort()
        res = (tasks[-1] - 1) * (n+1)
        i = len(tasks) - 1
        while i >= 0 and tasks[i] == tasks[-1]:
            i -= 1
            res += 1
        return res if res > length else length


class Solution2(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        da = dict()
        n += 1
        for t in tasks:
            da[t] = da.get(t, 0) + 1
        tasks = [[v, -n] for v in da.values()]
        ans = 0
        while tasks:
            cur = n
            i = 0
            tasks.sort(key=lambda o: o[0], reverse=True)
            while cur and i < len(tasks):
                task = tasks[i]
                if task[0] == 0:
                    tasks = tasks[:i]
                    break
                if ans - task[1] >= n:
                    task[1] = ans
                    task[0] -= 1
                    ans += 1
                    cur -= 1
                i += 1

            if cur and tasks and tasks[0][0]:
                ans += 1
        return ans



tasks, n = ["A","A","A","C","D","B","C","B","B","B"], 2#,"C","D"], 2
print(Solution().leastInterval(tasks, n))
