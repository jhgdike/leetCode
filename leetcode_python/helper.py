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


ListNode = List


def arr_to_list(nums):
    if not nums:
        return
    origin = List(nums[0])
    l = origin
    for num in nums[1:]:
        l.next = List(num)
        l = l.next
    return origin


def list_to_arr(list):
    arr = []
    while list:
        arr.append(list.val)
        list = list.next
    return arr


def form_tree(nums):
    length = len(nums)

    def add_node(node, i):
        if i < length and nums[i] is not None:
            node.left = TreeNode(nums[i])
            temp.append(node.left)
        if i + 1 < length and nums[i+1] is not None:
            node.right = TreeNode(nums[i+1])
            temp.append(node.right)

    if not nums:
        return
    root = TreeNode(nums[0])
    temp = [root]
    i = 1
    while i < length:
        node_stack = temp
        temp = []
        for node in node_stack:
            add_node(node, i)
            i += 2
    return root
