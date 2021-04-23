class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.nums = [0] * k
        self.count = 0
        self.left = 0
        self.right = -1
        self.cap = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.count += 1
            self.right = (self.right + 1) % self.cap
            self.nums[self.right] = value
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.count -= 1
            self.left = (self.left + 1) % self.cap
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.nums[self.left]
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.nums[self.right]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.cap == self.count

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
