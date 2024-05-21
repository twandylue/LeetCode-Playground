class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """time complexity: O(E+V), space complexity: O(V), where E is the number of edges and V is the number of vertices (nodes)"""
        result: list[int] = []
        safe: dict[int, bool] = {}
        for i in range(len(graph)):
            if self.dfs(i, safe, graph):
                result.append(i)
        return result

    def dfs(self, node: int, safe: dict[int, bool], graph: list[list[int]]) -> bool:
        if node in safe:
            return safe[node]
        safe[node] = False
        for neighbor in graph[node]:
            if not self.dfs(neighbor, safe, graph):
                return False
        safe[node] = True
        return True


def test_eventualSafeNodes_case_1():
    # arrange
    graph: list[list[int]] = [[1, 2], [2, 3], [5], [0], [5], [], []]
    expected: list[int] = [2, 4, 5, 6]

    # act
    solution = Solution()
    actual = solution.eventualSafeNodes(graph)

    # assert
    assert expected == actual


def test_eventualSafeNodes_case_2():
    # arrange
    graph: list[list[int]] = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    expected: list[int] = [4]

    # act
    solution = Solution()
    actual = solution.eventualSafeNodes(graph)

    # assert
    assert expected == actual
