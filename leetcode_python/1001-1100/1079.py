
from copy import copy
from collections import Counter


def fac(n):
    i = n
    while i > 1:
        i -= 1
        n *= i
    return n


def calc_com(com_list):
    com_list = [x for x in com_list if x > 0]
    total = fac(sum(com_list))
    for c in com_list:
        total /= fac(c)
    return total


def calc_all(com_list):
    com_list = [x for x in com_list if x > 0]
    if len(com_list) == 1:
        return calc_com(com_list)

    cur = calc_com(com_list)
    for i in range(len(com_list)):
        new_com = copy(com_list)
        new_com[i] -= 1
        cur += calc_all(new_com)
    return cur


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        c = Counter(tiles)
        return calc_all(c.values())
