# Definition for a Node.
from typing import Optional


# NOTE: time complexity: O(n), space complexity: O(n)
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Optional[Node]:
        if node is None:
            return None
        nodeMap: dict[Node, Node] = dict()
        n: Node = self.bfs(node, nodeMap)
        return n

    def bfs(self, node: Node, nodeMap: dict[Node, Node]) -> Node:
        if node in nodeMap:
            return nodeMap[node]
        newNode: Node = Node(node.val)
        nodeMap[node] = newNode
        for n in node.neighbors:
            newNode.neighbors.append(self.bfs(n, nodeMap))

        return newNode
