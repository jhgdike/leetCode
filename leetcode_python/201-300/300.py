class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        res = 0
        for i in range(len(nums)):
            max_val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_val = max(dp[j], max_val)
            dp[i] += max_val
            res = max(res, dp[i])
        return res

    def lengthOfLIS3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for n in nums:
            if len(res) == 0 or n > res[-1]:
                res.append(n)
            else:
                for i in range(len(res)):
                    if res[i] >= n:
                        res[i] = n
                        break
        print(res)
        return len(res)


print(Solution1().lengthOfLIS3([4,10,4,3,8,9]))
