class Node:
    def __init__(self, key):
        self.key = key
        self.parents = []
        # self.children = dict()
        self.is_end = False
        self.chain = []


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_dict = dict()
        tail = None
        for word in wordList:
            node = Node(word)
            word_dict[word] = node
            if word == endWord:
                tail = node
                tail.is_end = True
        if not tail:
            return []
        head = Node(beginWord)
        head.chain = [[beginWord]]
        dfs([head], wordList, word_dict)

        form_chain(tail)
        return tail.chain


def form_chain(node):
    if not node.parents or node.chain:
        return
    for p in node.parents:
        form_chain(p)
        node.chain.extend([c + [node.key] for c in p.chain])


def is_neighber(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
        if c > 1:
            return False
    return c == 1


def dfs(heads, left_words, word_dict):
    find = False
    new_left = []
    nodes = set()
    for word in left_words:
        use = False
        word_node = word_dict[word]
        for node in heads:
            if is_neighber(node.key, word):
                # node.children[word] = word_node
                nodes.add(word_node)
                word_node.parents.append(node)
                if not use:
                    use = True
        if not use:
            new_left.append(word)
        if word_node.is_end and use:
            find = True
    if find:
        return True
    # nodes = set()
    # for node in heads:
    #     for c in node.children.values():
    #         nodes.add(c)
    if not nodes:
        return False
    return dfs(list(nodes), new_left, word_dict)


# print(Solution().findLadders('a', 'c', ["a","b","c"]))
# print(Solution().findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(Solution().findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
