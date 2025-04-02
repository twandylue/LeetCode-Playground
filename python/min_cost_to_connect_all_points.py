import heapq


class DSU:
    def __init__(self, n: int):
        self._ranks: list[int] = [1] * n
        self._parents: list[int] = [i for i in range(n)]
        self._indep: int = n

    def find(self, n: int) -> int:
        while n != self._parents[n]:
            n = self._parents[n]
        return n

    def union(self, u: int, v: int) -> bool:
        pu: int = self.find(u)
        pv: int = self.find(v)
        if pu == pv:
            return False
        self._indep -= 1
        if self._ranks[pv] > self._ranks[pu]:
            pu, pv = pv, pu
        self._ranks[pu] += self._ranks[pv]
        self._parents[pv] = pu
        return True

    def get_indep(self) -> int:
        return self._indep


class Solution:
    def minCostConnectPoints2(self, points: list[list[int]]) -> int:
        """time complexity: O(n^2 log n)"""
        edges: list[tuple[int, int, int]] = []
        n: int = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i, n):
                x2, y2 = points[j]
                dist: int = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        dsu: DSU = DSU(n)
        result: int = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                result += dist
        return result

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
