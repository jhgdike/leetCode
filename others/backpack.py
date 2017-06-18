class Simple:

    def find_max_value(self, weights, values, w=5):
        n = len(weights)
        dp = [0] * (w + 1)
        for i in range(n):
            zero_one_pack(dp, weights[i], values[i], w)
        return dp[-1]


class Complete:

    def find_max_value(self, weights, values, w=5):
        n = len(weights)
        dp = [0] * (w + 1)
        for i in range(n):
            complete_pack(dp, weights[i], values[i], w)
        return dp[-1]


class Multiple:

    def find_max_value(self, weights, values, nums, w=5):
        n = len(weights)
        dp = [0] * (w + 1)
        for i in range(n):
            multiple_pack(dp, weights[i], values[i], nums[i], w)
        return dp[-1]


def zero_one_pack(dp, cost, value, capacity):
    """01 backpack"""
    for j in range(capacity, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + value)


def complete_pack(dp, cost, value, capacity):
    """complete backpack"""
    for j in range(cost, capacity + 1):
        dp[j] = max(dp[j], dp[j - cost] + value)


def multiple_pack(dp, cost, value, nums, capacity):
    """multiple backpack"""
    if cost * nums > capacity:
        complete_pack(dp, cost, value, capacity)
        return
    k = 1
    while k <= nums:
        zero_one_pack(dp, cost * k, value * k, capacity)
        nums -= k
        k *= 2
