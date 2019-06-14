# coding: utf-8

import time


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.expire_at = None  # When not set, the key-node will not expire.
        self.left = None
        self.right = None

    def is_expired(self):
        if not self.expire_at:
            return True
        return time.time() >= self.expire_at

    def set_expire_time(self, expire_time):
        self.expire_at = time.time() + expire_time


class LRUCache(object):
    """惰性删除lru"""

    def __init__(self, max_len=1000):
        self.max_len = max_len if max_len > 1 else 1
        self._dict = {}
        self._len = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.left = self.tail
        self.tail.right = self.head

    def get(self, key):
        node = self._dict.get(key)
        if not node:
            return
        if node.is_expired():
            self._remove_node(node)
            return
        self._refresh_node(node)
        return node.value

    def set(self, key, value, expire_time=1.0):
        node = self._dict.get(key)
        if not node:
            node = Node(key, value)
            self._add_node(node)
        else:
            node.value = value
            self._refresh_node(node)
        node.set_expire_time(expire_time)
        return True

    def __len__(self):
        return self._len

    def _remove_node(self, node):
        """remove node"""
        self._release_node_from_list(node)
        self._dict.pop(node.key)
        self._len -= 1

    def _add_node(self, node):
        """add mode"""
        if self._len >= self.max_len:
            self._remove_node(self.tail.right)
        self._dict[node.key] = node
        self._insert_node_at_head(node)
        self._len += 1

    def _refresh_node(self, node):
        """refresh_node"""
        self._release_node_from_list(node)
        self._insert_node_at_head(node)

    @staticmethod
    def _release_node_from_list(node):
        node.left.right = node.right
        node.right.left = node.left

    def _insert_node_at_head(self, node):
        self.head.left.right = node
        node.left = self.head.left

        self.head.left = node
        node.right = self.head


def test():
    lru = LRUCache(10)
    for i in range(10):
        lru.set('key_{}'.format(i), i)
    node = lru.tail.right
    while node.right:
        assert node.key == 'key_{}'.format(node.value)
        node = node.right
    print("continue set")
    for i in range(10, 20):
        lru.set('key_{}'.format(i), i, 0.1 * (i - 10))
    node = lru.tail.right
    while node.right:
        assert node.key == 'key_{}'.format(node.value)
        node = node.right
    assert lru.get('key_5') is None
    assert lru.get('key_15') == 15
    assert len(lru) == 10
    assert lru.head.left.value == 15
    time.sleep(0.55)
    assert lru.get('key_15') is None
    assert len(lru) == 9


if __name__ == '__main__':
    test()
