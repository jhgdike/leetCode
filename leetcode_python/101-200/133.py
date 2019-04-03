"""
# Definition for a Node.

"""


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # if not node:
        #     return
        root = Node(node.val, [])
        dict = {node.val: root}

        def dfs(cur, neighbors):

            # if cur:
            for nb in neighbors:
                if nb.val not in dict:
                    new_node = Node(nb.val, [])
                    dict[nb.val] = new_node
                    dfs(new_node, nb.neighbors)
                cur.neighbors.append(dict[nb.val])
        dfs(root, node.neighbors)
        return root
