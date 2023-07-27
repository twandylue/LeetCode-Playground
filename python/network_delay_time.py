import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        minHeap: list[tuple[int, int]] = [(0, k)]
        path: int = 0
        visited: set[int] = set()
        vertexMap: dict[int, list[tuple[int, int]]] = dict()
        for item in times:
            n1: int = item[0]
            n2: int = item[1]
            d: int = item[2]
            if n1 in vertexMap:
                vertexMap[n1].append((d, n2))
            else:
                vertexMap[n1] = [(d, n2)]

        while len(minHeap) > 0:
            d1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            path = max(path, d1)

            if n1 in vertexMap:
                for d2, n2 in vertexMap[n1]:
                    if n2 in visited:
                        continue
                    heapq.heappush(minHeap, (d1 + d2, n2))

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
