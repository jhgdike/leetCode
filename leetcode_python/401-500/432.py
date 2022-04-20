import random


class Entry:
    def __init__(self, key):
        self.next = [None] * 16
        self.level = 1
        self.pre = None
        self.key = key
        self.count = 1


class AllOne:

    def __init__(self):
        self.dict = dict()
        self.level = 0
        self.entry_head = Entry(None)
        self.entry_tail = Entry(None)
        self.entry_head.next = [self.entry_tail] * 16
        self.entry_tail.pre = self.entry_head
        self.total = 0

    def insert(self, entry):
        self.total += 1
        # if self.level == 0:
        #     self.entry_head.next[0] = entry
        #     self.level = 1
        #     entry.pre = self.entry_head
        #     return
        l = self.level
        prev = [self.entry_head] * 16
        start = self.entry_head
        while l > 0:
            while start.next[l - 1] is not self.entry_tail and (start.next[l - 1].count < entry.count or (start.next[l - 1].count == entry.count and start.next[l - 1].key < entry.key)):
                start = start.next[l-1]
            l -= 1
            prev[l] = start
        entry.pre = prev[0]
        entry.next = [self.entry_tail] * 16
        while l < 16:
            self.level = max(self.level, l+1)
            entry.level = l+1
            entry.next[l] = prev[l].next[l]
            if l == 0:
                prev[l].next[l].pre = entry
            prev[l].next[l] = entry
            if random.random() < 0.25:
                l += 1
            else:
                break

    def delete(self, entry):
        self.total -= 1
        l = self.level
        prev = [self.entry_head] * 16
        start = self.entry_head
        while l > 0:
            while start.next[l - 1] is not self.entry_tail and (start.next[l - 1].count < entry.count or (start.next[l - 1].count == entry.count and start.next[l - 1].key < entry.key)):
                start = start.next[l - 1]
            l -= 1
            prev[l] = start
        l = entry.level
        if entry.next[0]:
            entry.next[0].pre = entry.pre
        while l > 0:
            prev[l-1].next[l-1] = entry.next[l-1]
            l-=1

    def inc(self, key: str) -> None:
        entry = self.dict.get(key)
        if not entry:
            entry = Entry(key)
            self.dict[key] = entry
            self.insert(entry)
        else:
            entry = self.dict[key]
            entry.count += 1
            if entry.next[0] is self.entry_tail or entry.next[0].count > entry.count or (entry.next[0].count >= entry.count and entry.next[0].key > entry.key):
                return
            self.delete(entry)
            self.insert(entry)

    def dec(self, key: str) -> None:
        entry = self.dict[key]
        entry.count -= 1
        if entry.count == 0:
            self.dict.pop(key)
            self.delete(entry)
        else:
            if entry.pre is self.entry_head or entry.pre.count < entry.count or (entry.pre.count == entry.count and entry.pre.key < entry.key):
                return
            self.delete(entry)
            self.insert(entry)

    def getMaxKey(self) -> str:
        if len(self.dict) == 0:
            return ""
        return self.entry_tail.pre.key

    def getMinKey(self) -> str:
        if len(self.dict) == 0:
            return ""
        return self.entry_head.next[0].key



# Your AllOne object will be instantiated and called as such:
import time
start = time.time()
key = "hello"
obj = AllOne()
obj.inc(key)
obj.inc(key)
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("leet")
print(obj.getMaxKey())
print(obj.getMinKey())

print(time.time()-start)