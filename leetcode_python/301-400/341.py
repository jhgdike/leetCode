class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nest = nestedList
        self.has_next = len(nestedList) > 0
        def iter():
            def yield_list(lis, last):
                for i in range(len(lis)):
                    item = lis[i]
                    if isinstance(item, list):
                        for j in yield_list(item, last and i == len(lis)-1):
                            yield j
                    else:
                        if last and i == len(lis)-1:
                            self.has_next = False
                        yield item
            for i in yield_list(self.nest, True):
                yield i
        self.iter = iter()

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return next(self.iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next


it = NestedIterator([[1,1],2,[1,1]])
res = []
while it.hasNext():
    res.append(it.next())
print(res)
