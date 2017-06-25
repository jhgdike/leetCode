"""
Add and Search Word - Data structure design
***********
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = [0] * 26
        self.next = [None] * 26
        self.end = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            index = ord(word[0]) - ord('a')
            if not self.dic[index]:
                self.dic[index] = 1
            if len(word) > 1:
                if self.next[index] is None:
                    self.next[index] = WordDictionary()
                self.next[index].addWord(word[1:])
            else:
                self.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word:
            if word[0] != '.':
                index = ord(word[0]) - ord('a')
                if not self.dic[index]:
                    return False
                if len(word) > 1:
                    return self.next[index] is not None and self.next[index].search(word[1:])
                else:
                    return self.end
            else:
                if len(word) == 1:
                    return self.end
                for item in self.next:
                    if item and item.search(word[1:]):
                        return True
        return False


# a faster way to pass the testcase, but not a good way.
class WordDictionary2(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord('and')
# for item in [["at"],["and"],["an"],["add"],["a"]]:
#     obj.addWord(item[0])
# param_2 = [obj.search(item[0]) for item in [["an."],["b."],["a.d"],["."]]]
# print(param_2)