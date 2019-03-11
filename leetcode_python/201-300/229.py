class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1, c1, a2, c2 = 0, 0, 1, 0
        for n in nums:
            if a2 == n:
                c2 += 1
            elif a1 == n:
                c1 += 1
            elif c1 == 0:
                a1, c1 = n, 1

            elif c2 == 0:
                a2, c2 = n, 1

            else:
                c1, c2 = c1-1, c2-1
        n1, n2 = 0, 0
        for n in nums:
            if n == a1:
                n1 += 1
            elif n == a2:
                n2 += 1
        res = []
        if n1 > len(nums)//3:
            res.append(a1)
        if n2 > len(nums)//3:
            res.append(a2)
        return res


Solution().majorityElement([8,8,7,7,7])
Solution().majorityElement([1,2,2,3,2,1,1,3])
