class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        """time complexity: O(n * m), space complexity: O(n * m)"""
        visited: set[tuple[int, int]] = set()
        dircs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) in visited:
                    continue
                if self.dfs(r, c, (-1, -1), grid[r][c], dircs, visited, grid):
                    return True
        return False

    def dfs(
        self,
        r: int,
        c: int,
        prev: tuple[int, int],
        char: str,
        dircs: list[tuple[int, int]],
        visited: set[tuple[int, int]],
        grid: list[list[str]],
    ) -> bool:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] != char:
            return False
        if (r, c) in visited:
            return True
        visited.add((r, c))
        curr_char: str = grid[r][c]
        curr: tuple[int, int] = (r, c)
        for dr, dc in dircs:
            next_r: int = r + dr
            next_c: int = c + dc
            if (next_r, next_c) == prev:
                continue
            if self.dfs(next_r, next_c, curr, curr_char, dircs, visited, grid):
                return True
        return False


def test_containsCycle_case_1():
    # arrange
    grid: list[list[str]] = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
    expected: bool = False

    # act
    actual = Solution().containsCycle(grid)

    # assert
    assert expected == actual


def test_containsCycle_case_2():
    # arrange
    grid: list[list[str]] = [
        ["c", "c", "c", "a"],
        ["c", "d", "c", "c"],
        ["c", "c", "e", "c"],
        ["f", "c", "c", "c"],
    ]
    expected: bool = True

    # act
    actual = Solution().containsCycle(grid)

    # assert
    assert expected == actual


def test_containsCycle_case_3():
    # arrange
    grid: list[list[str]] = [["a", "a", "b"]]
    expected: bool = False

    # act
    actual = Solution().containsCycle(grid)

    # assert
    assert expected == actual
