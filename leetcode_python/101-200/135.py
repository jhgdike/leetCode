class Solution1(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left, right = [1] * n, [1] * n
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                left[i + 1] = left[i] + 1
            if ratings[n - i - 2] > ratings[n - i - 1]:
                right[n - i - 2] = right[n - i - 1] + 1
        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])
        return ans


class Solution2(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left = [1] * n
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                left[i + 1] = left[i] + 1
        ans = left[-1]
        right = 1
        for i in range(1, n):
            right = right + 1 if ratings[n - i - 1] > ratings[n - i] else 1
            ans += max(left[n - i - 1], right)

        return ans


class Solution3(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        ans = inc = pre = 1
        dec = 0
        for i in range(1, n):
            if ratings[i-1] <= ratings[i]:
                dec = 0
                inc = pre = 1 if ratings[i-1] == ratings[i] else pre + 1
                ans += pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ans += dec
                pre = 1

        return ans


s = Solution3()

print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
print(s.candy([1, 3, 2, 2, 1]))  # 7
print(s.candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]))  # 47
