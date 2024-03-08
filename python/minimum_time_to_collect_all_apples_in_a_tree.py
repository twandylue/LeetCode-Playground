import sys

sys.path.append("./models")
sys.path.append("./utils")

from typing import Optional
from binary_tree_node import TreeNode
from deserialize_to_binary_tree import DeserializeFromList
from serialize_binary_tree import SerializeBinaryTreeToList


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        """time complexity: O(n)"""
        adj: dict[int, list[int]] = {}
        for i in range(n):
            adj[i] = []
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)
        return self.dfs(0, -1, adj, hasApple)

    def dfs(
        self,
        curr: int,
        par: int,
        adj: dict[int, list[int]],
        hasApple: list[bool],
    ) -> int:
        """dfs"""
        time: int = 0
        for child in adj[curr]:
            if child == par:
                continue
            child_time = self.dfs(child, curr, adj, hasApple)
            if child_time != 0 or hasApple[child]:
                time += 2 + child_time
        return time


def test_minTime_case_1():
    # arrange
    n: int = 7
    edges: list[list[int]] = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple: list[bool] = [False, False, True, False, True, True, False]
    expected: int = 8

    # act
    solution = Solution()
    actual = solution.minTime(n, edges, hasApple)

    # assert
    assert expected == actual


def test_minTime_case_2():
    # arrange
    n: int = 7
    edges: list[list[int]] = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple: list[bool] = [False, False, True, False, False, True, False]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.minTime(n, edges, hasApple)

    # assert
    assert expected == actual
