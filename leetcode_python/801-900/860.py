class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bil = [0, 0]
        for b in bills:
            if b == 5:
                bil[0] += 1
            elif b == 10:
                if bil[0] < 1:
                    return False
                bil[0] -= 1
                bil[1] += 1
            else:
                if bil[0] < 1 or (bil[0] < 3 and bil[1] < 1):
                    return False
                if bil[1]:
                    bil[1] -= 1
                    bil[0] -= 1
                else:
                    bil[0] -= 3
        return True

print(Solution().lemonadeChange([5,5,5,10,20]))
