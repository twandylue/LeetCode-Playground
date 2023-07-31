import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        cost: int = 0
        visited: set[int] = set()
        adj_nodes: dict[int, list[tuple[int, int]]] = dict()
        min_heap: list[tuple[int, int]] = []

        for i in range(0, len(points)):
            x1: int = points[i][0]
            y1: int = points[i][1]
            for j in range(i + 1, len(points)):
                x2: int = points[j][0]
                y2: int = points[j][1]
                d: int = abs(x1 - x2) + abs(y1 - y2)
                if i in adj_nodes:
                    adj_nodes[i].append((d, j))
                else:
                    adj_nodes[i] = [(d, j)]

                if j in adj_nodes:
                    adj_nodes[j].append((d, i))
                else:
                    adj_nodes[j] = [(d, i)]

        min_heap = [(0, 0)]
        while len(visited) != len(points):
            if len(min_heap) > 0:
                d, n = heapq.heappop(min_heap)
                if n in visited:
                    continue
                visited.add(n)
                cost += d
                if n in adj_nodes:
                    for node in adj_nodes[n]:
                        if node in visited:
                            continue
                        heapq.heappush(min_heap, node)

        return cost


def test_minCostConnectPoints_case_1():
    # arrange
    points: list[list[int]] = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    expected: int = 20

    # act
    solution = Solution()
    actual = solution.minCostConnectPoints(points)

    # assert
    assert actual == expected


def test_minCostConnectPoints_case_2():
    # arrange
    points: list[list[int]] = [[3, 12], [-2, 5], [-4, 1]]
    expected: int = 18

    # act
    solution = Solution()
    actual = solution.minCostConnectPoints(points)

    # assert
    assert actual == expected
