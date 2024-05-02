class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        """time complexity: O(n), space complexity: O(n), where n is the number of cells in grid2"""
        count: int = 0
        visited: set[tuple[int, int]] = set()
        for r in range(len(grid2)):
            for c in range(len(grid2[r])):
                if (
                    grid2[r][c] == 1
                    and (r, c) not in visited
                    and self.dfs(r, c, grid1, grid2, visited)
                ):
                    count += 1
        return count

    def dfs(
        self,
        r: int,
        c: int,
        grid1: list[list[int]],
        grid2: list[list[int]],
        visited: set[tuple[int, int]],
    ) -> bool:
        if (
            r < 0
            or r == len(grid2)
            or c < 0
            or c == len(grid2[r])
            or grid2[r][c] == 0
            or (r, c) in visited
        ):
            return True
        visited.add((r, c))
        result: bool = True
        if grid1[r][c] == 0:
            result = False
        result = self.dfs(r - 1, c, grid1, grid2, visited) and result
        result = self.dfs(r + 1, c, grid1, grid2, visited) and result
        result = self.dfs(r, c - 1, grid1, grid2, visited) and result
        result = self.dfs(r, c + 1, grid1, grid2, visited) and result
        return result

        ## BUG: This is "not" the same as the above code
        # result = result and self.dfs(r - 1, c, grid1, grid2, visited)
        # result = result and self.dfs(r + 1, c, grid1, grid2, visited)
        # result = result and self.dfs(r, c - 1, grid1, grid2, visited)
        # result = result and self.dfs(r, c + 1, grid1, grid2, visited)
        # return result

        ## BUG: This is "not" the same as the above code
        # return (
        #     self.dfs(r - 1, c, grid1, grid2, visited)
        #     and self.dfs(r + 1, c, grid1, grid2, visited)
        #     and self.dfs(r, c - 1, grid1, grid2, visited)
        #     and self.dfs(r, c + 1, grid1, grid2, visited)
        #     and result
        # )


def test_countSubIslands_case_1():
    # arrange
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.countSubIslands(grid1, grid2)

    # assert
    assert expected == actual


def test_countSubIslands_case_2():
    # arrange
    grid1 = [
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
    ]
    grid2 = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.countSubIslands(grid1, grid2)

    # assert
    assert expected == actual
