from collections import defaultdict, deque


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        """time complexity: O(V + E)"""
        adj: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue: deque[int] = deque([source])
        visited: set[int] = set([source])
        while len(queue) > 0:
            node: int = queue.popleft()
            if node == destination:
                return True
            for nei in adj[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                queue.append(nei)
        return False


def test_validPath_case_1():
    # arrange
    n: int = 3
    edges: list[list[int]] = [[0, 1], [1, 2], [2, 0]]
    source: int = 0
    destination: int = 2
    expected: bool = True

    # act
    actual = Solution().validPath(n, edges, source, destination)

    # assert
    assert expected == actual


def test_validPath_case_2():
    # arrange
    n: int = 6
    edges: list[list[int]] = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source: int = 0
    destination: int = 5
    expected: bool = False

    # act
    actual = Solution().validPath(n, edges, source, destination)

    # assert
    assert expected == actual
