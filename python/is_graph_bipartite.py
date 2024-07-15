from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """time complexity: O(n + m), where n is the number of nodes and m is the number of edges. space complexity: O(n)"""
        odd: list[int] = [0] * len(graph)  # odd = 1 and even = -1
        for i in range(len(graph)):
            if not self.bfs(i, odd, graph):
                return False
        return True

    def bfs(self, node: int, odd: list[int], graph: list[list[int]]) -> bool:
        if odd[node] == 1:
            return True
        odd[node] = -1
        queue: deque[int] = deque([node])
        while len(queue) > 0:
            i: int = queue.popleft()
            for nei in graph[i]:
                if odd[i] == odd[nei]:
                    return False
                elif odd[nei] == 0:
                    queue.append(nei)
                    odd[nei] = -1 * odd[i]
        return True


def test_isBipartite_case_1():
    # arrange
    graph: list[list[int]] = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isBipartite(graph)

    # assert
    assert expected == actual


def test_isBipartite_case_2():
    # arrange
    graph: list[list[int]] = [[1, 3], [0, 2], [1, 3], [0, 2]]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isBipartite(graph)

    # assert
    assert expected == actual


def test_isBipartite_case_3():
    # arrange
    graph: list[list[int]] = [
        [],
        [2, 4, 6],
        [1, 4, 8, 9],
        [7, 8],
        [1, 2, 8, 9],
        [6, 9],
        [1, 5, 7, 8, 9],
        [3, 6, 9],
        [2, 3, 4, 6, 9],
        [2, 4, 5, 6, 7, 8],
    ]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isBipartite(graph)

    # assert
    assert expected == actual


def test_isBipartite_case_3():
    # arrange
    graph: list[list[int]] = [
        [],
        [2, 4, 6],
        [1, 4, 8, 9],
        [7, 8],
        [1, 2, 8, 9],
        [6, 9],
        [1, 5, 7, 8, 9],
        [3, 6, 9],
        [2, 3, 4, 6, 9],
        [2, 4, 5, 6, 7, 8],
    ]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isBipartite(graph)

    # assert
    assert expected == actual
