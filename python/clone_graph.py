from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # NOTE: time complexity: O(n), space complexity: O(n), where n is the number of nodes in the graph
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        new_node_map: dict[Node, Node] = {}
        new_node: Node = self.dfs(node, new_node_map)
        return new_node

    def dfs(self, node: Node, new_node_map: dict[Node, Node]) -> Node:
        if node in new_node_map:
            return new_node_map[node]
        new_node: Node = Node(node.val)
        new_node_map[node] = new_node
        for n in node.neighbors:
            new_node.neighbors.append(self.dfs(n, new_node_map))
        return new_node
