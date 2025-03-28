import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """time complexity: O(E log V), where E is the number of edges and V is the number of vertices, space complexity: O(V)"""
        result: int = 0
        adj: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        visited: set[int] = set()
        min_heap: list[tuple[int, int]] = [(0, k)]
        while len(min_heap) > 0:
            accu, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            result = accu
            for nei, nei_time in adj[node]:
                heapq.heappush(min_heap, (result + nei_time, nei))
        return result if len(visited) == n else -1


def test_networkDelayTime_case_1():
    # arrange
    times: list[list[int]] = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n: int = 4
    k: int = 2
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.networkDelayTime(times, n, k)

    # assert
    assert expected == actual


def test_networkDelayTime_case_2():
    # arrange
    times: list[list[int]] = [[1, 2, 1]]
    n: int = 2
    k: int = 1
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.networkDelayTime(times, n, k)

    # assert
    assert expected == actual


def test_networkDelayTime_case_3():
    # arrange
    times: list[list[int]] = [[1, 2, 1]]
    n: int = 2
    k: int = 2
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.networkDelayTime(times, n, k)

    # assert
    assert expected == actual


def test_networkDelayTime_case_4():
    # arrange
    times: list[list[int]] = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    n: int = 3
    k: int = 1
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.networkDelayTime(times, n, k)

    # assert
    assert expected == actual
