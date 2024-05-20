class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        edges: set[tuple[int, int]] = {(fr, to) for fr, to in connections}
        graph: dict[int, list[int]] = {}
        visited: set[int] = set()
        changes: list[int] = [0]
        for city in range(n):
            if city not in graph:
                graph[city] = []
        for fr, to in connections:
            if fr not in graph:
                graph[fr] = [to]
            else:
                graph[fr].append(to)
            if to not in graph:
                graph[to] = [fr]
            else:
                graph[to].append(fr)
        visited.add(0)
        self.dfs(0, edges, graph, visited, changes)
        return changes[0]

    def dfs(
        self,
        city: int,
        edges: dict[int, int],
        graph: dict[int, list[int]],
        visited: set[int],
        changes: list[int],
    ) -> None:
        for neighbor in graph[city]:
            if neighbor in visited:
                continue
            if (neighbor, city) not in edges:
                changes[0] += 1
            visited.add(neighbor)
            self.dfs(neighbor, edges, graph, visited, changes)


def test_minReorder_case_1():
    # arrange
    n: int = 6
    connections: list[list[int]] = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.minReorder(n, connections)

    # assert
    assert expected == actual


def test_minReorder_case_2():
    # arrange
    n: int = 5
    connections: list[list[int]] = [[1, 0], [1, 2], [3, 2], [3, 4]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minReorder(n, connections)

    # assert
    assert expected == actual
