# coding: utf-8

"""
台阶问题:

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# 方法一
fibn = lambda n: n if n <= 2 else fibn(n-1) + fibn(n-2)


# 方法二
def memo(func):
    cache = {}

    def warp(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return warp


# 方法三
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a+b
    return fib


"""
变态台阶问题:

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
fibnn = lambda n: n if n < 2 else 2 * fibnn(n-1)
