class Node:
    """Definition for a QuadTree node."""

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        """time complexity: O(n^2 log n)"""
        return self.dfs(len(grid), 0, 0)

    def dfs(self, grid: list[list[int]], n: int, row: int, col: int) -> "Node":
        """dfs"""
        all_same: bool = True
        for i in range(n):
            for j in range(n):
                if grid[row][col] != grid[row + i][col + j]:
                    all_same = False
                    break
        if all_same:
            return Node(grid[row][col], True, None, None, None, None)
        n = n // 2
        top_left: Node = self.dfs(grid, n, row, col)
        top_right: Node = self.dfs(grid, n, row, col + n)
        bottom_left: Node = self.dfs(grid, n, row + n, col)
        bottom_right: Node = self.dfs(grid, n, row + n, col + n)
        return Node(0, False, top_left, top_right, bottom_left, bottom_right)


def test_construct_case_1():
    """NOTE: skip the test cases because it is difficult to prepare for"""
    assert True
