from collections import deque


class DSU:
    def __init__(self, n: int):
        self._comp: int = n
        self._parent: list[int] = [i for i in range(n + 1)]
        self._rank: list[int] = [1] * n

    def find(self, node: int) -> int:
        if self._parent[node] != node:
            self._parent[node] = self.find(self._parent[node])
        return self._parent[node]

    def union(self, u: int, v: int) -> bool:
        ru: int = self.find(u)
        rv: int = self.find(v)
        if ru == rv:
            return False
        self._comp -= 1
        if self._rank[ru] < self._rank[rv]:
            ru, rv = rv, ru
        self._rank[ru] += self._rank[rv]
        self._parent[rv] = ru
        return True

    def components(self) -> int:
        return self._comp


class Solution:
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) == 0 and n == 0:
            return True

        visited: set[int] = set()
        graph: dict[int, list[int]] = dict()
        for edge in edges:
            s: int = edge[0]
            e: int = edge[1]
            if s in graph:
                graph[s].append(e)
            else:
                graph[s] = [e]
            if e in graph:
                graph[e].append(s)
            else:
                graph[e] = [s]

        return self.walk(0, -1, visited, graph) and n == len(visited)

    def walk(
        self, node: int, preNode: int, visited: set[int], graph: dict[int, list[int]]
    ) -> bool:
        if node in visited:
            return False

        visited.add(node)
        if node in graph:
            for nextNode in graph[node]:
                if nextNode == preNode:
                    continue
                if self.walk(nextNode, node, visited, graph):
                    continue

                return False

        return True

    def valid_tree2(self, n: int, edges: list[list[int]]) -> bool:
        """time complexity: O(V + E)"""
        if len(edges) > (n - 1):
            return False
        visited: set[tuple[int, int]] = set()
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue: deque[tuple[int, int]] = deque([(0, -1)])
        visited.add(0)
        while len(queue) > 0:
            curr, parent = queue.popleft()
            visited.add(curr)
            for nei in adj[curr]:
                if parent == nei:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, curr))
        return len(visited) == n

    def valid_tree3(self, n: int, edges: list[list[int]]) -> bool:
        """time complexity: O(V + (E * a(V))"""
        if len(edges) > (n - 1):
            return False
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                continue
            return False
        return dsu.components() == 1


def test_valid_tree_case_1():
    # arrange
    n: int = 5
    edges: list[list[int]] = [[0, 1], [0, 2], [0, 3], [1, 4]]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.valid_tree(n, edges)

    # assert
    assert expected == actual


def test_valid_tree_case_2():
    # arrange
    n: int = 5
    edges: list[list[int]] = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.valid_tree(n, edges)

    # assert
    assert expected == actual
