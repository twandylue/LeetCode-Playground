from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """time complexity: O(n), space complexity: O(n), where n is the number of nodes in the graph"""
        node_map: dict[Node, Node] = {}
        new_head: Optional[Node] = self.dfs(node, node_map)
        return new_head

    def dfs(self, node: Optional[Node], node_map: dict[Node, Node]) -> Optional[Node]:
        if node is None:
            return None
        if node in node_map:
            return node_map[node]
        new_node: Node = Node(node.val)
        node_map[node] = new_node
        for nei in node.neighbors:
            new_node.neighbors.append(self.dfs(nei, node_map))
        return new_node
