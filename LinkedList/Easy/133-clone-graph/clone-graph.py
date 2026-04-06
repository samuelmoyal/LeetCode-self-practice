"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None
        mapping = {}
        origin = Node(node.val)
        mapping[node] = origin
        to_visit = [node]
        while to_visit:
            cur = to_visit.pop()
            cur_clone = mapping[cur] 

            for neighbour in cur.neighbors:
                if neighbour not in mapping:
                    mapping[neighbour] = Node(neighbour.val)
                    to_visit.append(neighbour)
                cur_clone.neighbors.append(mapping[neighbour])

        return origin



        """
        :type node: Node
        :rtype: Node
        """
        