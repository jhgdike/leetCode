class Solution:
    def countPalindromicSubsequences(self, S):
        from collections import defaultdict
        import bisect
        M = 1000000007
        characters = defaultdict(list)
        for idx, s in enumerate(S):
            characters[s].append(idx)
        # print(characters)
        lookup = {}

        def helper(i, j):
            if i >= j: return 0
            if (i, j) in lookup:
                return lookup[(i, j)]
            res = 0
            for c, v in characters.items():
                # print(c, v)
                n = len(v)
                new_i = None
                idx_i = bisect.bisect_left(v, i)
                if idx_i < n:
                    new_i = v[idx_i]
                if new_i == None or new_i >= j:
                    continue
                idx_j = bisect.bisect_left(v, j) - 1
                new_j = v[idx_j]
                res += helper(new_i + 1, new_j) + 2 if new_i != new_j else 1
            lookup[(i, j)] = res % M
            # print(lookup)
            return lookup[(i, j)]

        return helper(0, len(S))


class Solution2(object):

    def countPalindromicSubsequences(self, s):
        m = int(1e9 + 7)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for ln in range(1, n + 1):
            for i in range(n - ln):
                j = i + ln
                if s[i] == s[j]:
                    left = i + 1
                    right = j - 1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                    if left > right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif left == right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                dp[i][j] = dp[i][j] + m if dp[i][j] < 0 else dp[i][j] % m
        return dp[0][n - 1]


"""
我们再来看一种迭代的写法，使用一个二维的dp数组，其中dp[i][j]表示子字符串[i, j]中的不同回文子序列的个数，我们初始化dp[i][i]为1，因为任意一个单个字符就是一个回文子序列，其余均为0。这里的更新顺序不是正向，也不是逆向，而是斜着更新，对于”bccb”的例子，其最终dp数组如下，我们可以看到其更新顺序分别是红-绿-蓝-橙。

b c c b 
b 1 2 3 6 
c 0 1 2 3 
c 0 0 1 2 
b 0 0 0 1

这样更新的好处是，更新当前位置时，其左，下，和左下位置的dp值均已存在，而当前位置的dp值需要用到这三个位置的dp值。我们观察上面的dp数组，可以发现当S[i]不等于S[j]的时候，dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]，即当前的dp值等于左边值加下边值减去左下值，因为算左边值的时候包括了左下的所有情况，而算下边值的时候也包括了左下值的所有情况，那么左下值就多算了一遍，所以要减去。而当S[i]等于S[j]的时候，情况就比较复杂了，需要分情况讨论，因为我们不知道中间还有几个和S[i]相等的值。举个简单的例子，比如”aba”和”aaa”，当i = 0, j = 2的时候，两个字符串均有S[i] == S[j]，此时二者都新增两个子序列”a”和”aa”，但是”aba”中间的”b”就可以加到结果res中，而”aaa”中的”a”就不能加了，因为和外层的单独”a”重复了。我们的目标就要找到中间重复的”a”。所以我们让left = i + 1, right = j - 1，然后对left进行while循环，如果left <= right, 且S[left] != S[i]的时候，left向右移动一个；同理，对right进行while循环，如果left <= right, 且S[right] != S[i]的时候，left向左移动一个。这样最终left和right值就有三种情况：

当left > righ时，说明中间没有和S[i]相同的字母了，就是”aba”这种情况，那么就有dp[i][j] = dp[i + 1][j - 1] * 2 + 2，其中dp[i + 1][j - 1]是中间部分的回文子序列个数，为啥要乘2呢，因为中间的所有子序列可以单独存在，也可以再外面包裹上字母a，所以是成对出现的，要乘2。加2的原因是外层的”a”和”aa”也要统计上。

当left = right时，说明中间只有一个和S[i]相同的字母，就是”aaa”这种情况，那么有dp[i][j] = dp[i + 1][j - 1] * 2 + 1，其中乘2的部分跟上面的原因相同，加1的原因是单个字母”a”的情况已经在中间部分算过了，外层就只能再加上个”aa”了。

当left < right时，说明中间至少有两个和S[i]相同的字母，就是”aabaa”这种情况，那么有dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]，其中乘2的部分跟上面的原因相同，要减去left和right中间部分的子序列个数的原因是其被计算了两遍，要将多余的减掉。
--------------------- 
作者：JackZhangNJU 
来源：CSDN 
原文：https://blog.csdn.net/JackZhang_123/article/details/78889242 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
