from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        """time complexity: O(n + m), where n is the number of nodes and m is the number of nodes"""
        answer: list[int] = [-1 for _ in range(n)]
        red_graph: dict[int, list[int]] = defaultdict(list)
        blue_graph: dict[int, list[int]] = defaultdict(list)
        for src, dst in redEdges:
            red_graph[src].append(dst)
        for src, dst in blueEdges:
            blue_graph[src].append(dst)
        queue: deque[tuple[int, int, str]] = deque()
        queue.append((0, 0, ""))
        visited: set[tuple[int, str]] = set()
        visited.add((0, ""))
        while len(queue) > 0:
            node, length, prev = queue.popleft()
            if answer[node] == -1:
                answer[node] = length
            if prev != "RED":
                for nei in red_graph[node]:
                    if (nei, "RED") not in visited:
                        queue.append((nei, length + 1, "RED"))
                        visited.add((nei, "RED"))
            if prev != "BLUE":
                for nei in blue_graph[node]:
                    if (nei, "BLUE") not in visited:
                        queue.append((nei, length + 1, "BLUE"))
                        visited.add((nei, "BLUE"))
        return answer


def test_shortestAlternatingPaths_case_1():
    # arrange
    n: int = 3
    redEdges: list[list[int]] = [[0, 1], [1, 2]]
    blueEdges: list[list[int]] = []
    expected: list[int] = [0, 1, -1]

    # act
    solution = Solution()
    actual = solution.shortestAlternatingPaths(n, redEdges, blueEdges)

    # assert
    assert actual == expected


def test_shortestAlternatingPaths_case_2():
    # arrange
    n: int = 3
    redEdges: list[list[int]] = [[0, 1]]
    blueEdges: list[list[int]] = [[2, 1]]
    expected: list[int] = [0, 1, -1]

    # act
    solution = Solution()
    actual = solution.shortestAlternatingPaths(n, redEdges, blueEdges)

    # assert
    assert actual == expected


def test_shortestAlternatingPaths_case_3():
    # arrange
    n: int = 3
    redEdges: list[list[int]] = [[0, 1], [0, 2]]
    blueEdges: list[list[int]] = [[1, 0]]
    expected: list[int] = [0, 1, 1]

    # act
    solution = Solution()
    actual = solution.shortestAlternatingPaths(n, redEdges, blueEdges)

    # assert
    assert actual == expected
