from collections import defaultdict
import math


class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        """time complexity: O(n), where n is the number of roads. space complexity: O(n)"""
        graph: dict[int, list[int]] = defaultdict(list)
        for src, des in roads:
            graph[src].append(des)
            graph[des].append(src)
        result: list[0] = [0]
        self.dfs(0, -1, seats, result, graph)
        return result[0]

    def dfs(
        self,
        node: int,
        parent: int,
        seats: int,
        result: list[int],
        graph: dict[int, list[int]],
    ) -> int:
        passengers: int = 0
        for child in graph[node]:
            if child != parent:
                p: int = self.dfs(child, node, seats, result, graph)
                passengers += p
                result[0] += int(math.ceil(p / seats))
        return passengers + 1


def test_minimumFuelCost_case_1():
    # arrange
    roads: list[list[int]] = [[0, 1], [0, 2], [0, 3]]
    seats: int = 5
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.minimumFuelCost(roads, seats)

    # assert
    assert expected == actual


def test_minimumFuelCost_case_2():
    # arrange
    roads: list[list[int]] = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
    seats: int = 2
    expected: int = 7

    # act
    solution = Solution()
    actual = solution.minimumFuelCost(roads, seats)

    # assert
    assert expected == actual
