from collections import deque
from copy import deepcopy
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # each node of the old graph will be mapped 1-to-1 to each in the new graph
        node_mapping = {}  

        def dfs(this_node):
            if this_node in node_mapping:       # node already copied
                return node_mapping[this_node]


            node_copy = Node(this_node.val)
            node_mapping[this_node] = node_copy  # add a new mapping
            for neigh in this_node.neighbors:
                node_copy.neighbors.append(dfs(neigh))

            
            return node_copy  # return the copy of the current node
        # end of dfs function

        return dfs(node) if node else None
        
    