class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i] = max([[]] + [dp[j] for j in range(i) if nums[i] % nums[j] == 0], key=len) + [nums[i]]
        return max(dp, key=len)


class Solution2(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}

        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}

        return list(max(subsets.values(), key=len))


class Solution3(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {}
        nums.sort()

        for i in range(len(nums)):
            subsets[i] = max([subsets[k] for k in subsets if nums[i] % nums[k] == 0] + [0]) + 1
        maxSize, maxSizeIndex = max([(v, i) for i, v in subsets.items()])
        ret = []

        """ Reconstruct the largest divisible subset """
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == subsets[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]


        return ret[::-1]


s = Solution3()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4,8]))
print(s.largestDivisibleSubset([1,2,7,8]))
print(s.largestDivisibleSubset([1,2,7,8,14,16,56]))
