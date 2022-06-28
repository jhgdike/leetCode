class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = list(str(num))
        def help(arr):
            if len(arr) <= 1:
                return arr
            ma = max(arr)
            if ma == arr[0]:
                return [ma] + help(arr[1:])
            tmp = arr[0]
            arr[0] = ma
            for i in range(len(arr)-1, -1, -1):
                if arr[i] == ma:
                    arr[i] = tmp
                    break
            return arr
        arr = help(arr)
        return int(''.join(arr))


print(Solution().maximumSwap(98368))