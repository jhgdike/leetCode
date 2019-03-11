class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = '1'
        if n == 1:
            return base
        while n > 1:
            base = self.generate(base)
            n -= 1
        return base

    def generate(self, base):
        gen = ''
        length = len(base)
        i = 1
        fir = base[0]
        time = 1
        while i < length:
            if fir == base[i]:
                time += 1
            else:
                gen += str(time) + fir
                fir = base[i]
                time = 1
            i += 1
        return gen + str(time) + fir


class Solution2(object):
    def countAndSay(self, n):
        import re
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
                       s)
        return s

    def countAndSay2(self, n):
        import re
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

    def countAndSay3(self, n):
        import itertools
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s