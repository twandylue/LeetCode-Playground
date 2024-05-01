import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """time complexity: O(E log V), where E is the number of edges and V is the number of vertices, space complexity: O(V)"""
        path: int = 0
        graph: dict[int, list[tuple[int, int]]] = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))
        min_heap: list[tuple[int, int]] = [(0, k)]
        visited: set[int] = set()
        while len(min_heap) > 0:
            accu_dis, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            path = max(path, accu_dis)
            visited.add(node)
            if node not in graph:
                continue
            for next_node, weight in graph[node]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (accu_dis + weight, next_node))
        return path if len(visited) == n else -1


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
