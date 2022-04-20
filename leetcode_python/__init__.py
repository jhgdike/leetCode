import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        tmp = [root]
        has = True
        while has:
            cur = []
            has = False
            for t in tmp:
                if t:
                    has = True
                    res.append(t.val)
                    cur.extend((t.left, t.right))
                else:
                    res.append(None)
                    cur.extend((None, None))
            tmp = cur
        while res and res[-1] is None:
            res = res[:-1]
        return json.dumps(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = json.loads(data)
        if len(l) == 0:
            return None
        root = TreeNode(l[0])
        tmp = [root]
        idx = 1
        while idx < len(l):
            cur = []
            for i in range(len(tmp)):
                if idx + i * 2 < len(l) and l[idx + i * 2] is not None:
                    tmp[i].left = TreeNode(l[idx + i * 2])
                    cur.append(tmp[i].left)
                else:
                    cur.append(None)
                if idx + i * 2 + 1 < len(l) and l[idx + i * 2 + 1] is not None:
                    tmp[i].right = TreeNode(l[idx + i * 2 + 1])
                    cur.append(tmp[i].right)
                else:
                    cur.append(None)
            idx += 2 * len(tmp)
            tmp = cur
        return root


c = Codec()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.right.left = TreeNode(4)
r.right.right = TreeNode(5)
raw = c.serialize(r)
print(raw)
c.deserialize(raw)
