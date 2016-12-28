# coding: utf-8

"""
创建数据结构的各种方法
"""

from __future__ import unicode_literals


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class List(object):
    def __init__(self, x):
        self.val = x
        self.next = None
