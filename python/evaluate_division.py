from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        """time complexity: O(n * (V + E))"""
        adj: dict[str, list[tuple[str, float]]] = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            adj[u].append((v, values[i]))
            adj[v].append((u, 1 / values[i]))
        return [self.bfs(s, t, adj) for s, t in queries]

    def bfs(
        self, source: str, target: str, adj: list[str, list[tuple[str, float]]]
    ) -> float:
        """time complexity: O(V + E)"""
        if source not in adj or target not in adj:
            return -1
        visited: set[str] = set([source])
        queue: deque[tuple[str, float]] = deque([(source, 1)])
        while len(queue) > 0:
            node, w = queue.popleft()
            if node == target:
                return w
            for nei, weight in adj[node]:
                if nei in visited:
                    continue
                queue.append((nei, w * weight))
                visited.add(nei)
        return -1


def test_calcEquation_case_1():
    # arrange
    equations: list[list[str]] = [["a", "b"], ["b", "c"]]
    values: list[float] = [2.0, 3.0]
    queries: list[list[str]] = [
        ["a", "c"],
        ["b", "a"],
        ["a", "e"],
        ["a", "a"],
        ["x", "x"],
    ]
    expected: list[float] = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    # act
    actual = Solution().calcEquation(equations, values, queries)

    # assert
    assert expected == actual


def test_calcEquation_case_2():
    # arrange
    equations: list[list[str]] = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values: list[float] = [1.5, 2.5, 5.0]
    queries: list[list[str]] = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected: list[float] = [3.75000, 0.40000, 5.00000, 0.20000]

    # act
    actual = Solution().calcEquation(equations, values, queries)

    # assert
    assert expected == actual


def test_calcEquation_case_3():
    # arrange
    equations: list[list[str]] = [["a", "b"]]
    values: list[float] = [0.5]
    queries: list[list[str]] = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected: list[float] = [0.50000, 2.00000, -1.00000, -1.00000]

    # act
    actual = Solution().calcEquation(equations, values, queries)

    # assert
    assert expected == actual
