class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        ans = [0] * n
        ans[-1] = -1
        st = list()
        st.append(n-1)
        for i in range(n-2, -1, -1):
            while st:
                if cars[i][1] <= cars[st[-1]][1] or (ans[st[-1]] >1e-9 and float(cars[st[-1]][0] - cars[i][0]) / (cars[st[-1]][1]-cars[i][1])):
                    st.pop()
                else:
                    break
            if st:
                ans[i] = float(cars[st[-1]][0] - cars[i][0]) / float(cars[i][1] - cars[st[-1]][1])
            else:
                ans[i] = -1
            st.append(i)

        return ans
