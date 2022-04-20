class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        c = self.highBit(data[0])
        if len(data) < c or c == 1 or c > 4:
            return False
        if c == 0:
            if len(data) == 1:
                return True
            return self.validUtf8(data[1:])
        for i in range(1, c):
            if data[i] & 0xc0 != 0x80:
                return False
        return True if c == len(data) else self.validUtf8(data[c:])

    def highBit(self, v: int):
        count = 0
        while v & 0x80:
            v <<= 1
            count += 1
        return count
