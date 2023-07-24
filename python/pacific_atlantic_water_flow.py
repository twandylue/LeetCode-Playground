class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        result: list[list[int]] = []
        pac: set[tuple[int, int]] = set()
        alt: set[tuple[int, int]] = set()
        rows: int = len(heights)
        cols: int = len(heights[0])

        for r in range(0, rows):
            self.dfs(r, 0, pac, heights, heights[r][0])
            self.dfs(r, cols - 1, alt, heights, heights[r][cols - 1])

        for c in range(0, cols):
            self.dfs(0, c, pac, heights, heights[0][c])
            self.dfs(rows - 1, c, alt, heights, heights[rows - 1][c])

        for r in range(0, rows):
            for c in range(0, cols):
                if (r, c) in pac and (r, c) in alt:
                    result.append([r, c])

        return result

    def dfs(
        self,
        r: int,
        c: int,
        visited: set[tuple[int, int]],
        heights: list[list[int]],
        pre_height: int,
    ) -> None:
        if (
            r < 0
            or r >= len(heights)
            or c < 0
            or c >= len(heights[0])
            or (r, c) in visited
            or heights[r][c] < pre_height
        ):
            return None

        visited.add((r, c))
        self.dfs(r + 1, c, visited, heights, heights[r][c])
        if r > 0:
            self.dfs(r - 1, c, visited, heights, heights[r][c])

        self.dfs(r, c + 1, visited, heights, heights[r][c])
        if c > 0:
            self.dfs(r, c - 1, visited, heights, heights[r][c])


def test_pacificAtlantic_case_1():
    # arrange
    heights: list[list[int]] = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    expected: list[list[int]] = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    # act
    solution = Solution()
    actual = solution.pacificAtlantic(heights)

    # assert
    assert expected == actual


def test_pacificAtlantic_case_2():
    # arrange
    heights: list[list[int]] = [
        [1],
    ]
    expected: list[list[int]] = [[0, 0]]

    # act
    solution = Solution()
    actual = solution.pacificAtlantic(heights)

    # assert
    assert expected == actual
