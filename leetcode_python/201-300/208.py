class Node(object):

    def __init__(self, val, is_leaf=False):
        self.children = {}
        self.val = val
        self.is_leaf = is_leaf


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if not word:
            return
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = Node(i)
            cur = cur.children[i]
        cur.is_leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.is_leaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
