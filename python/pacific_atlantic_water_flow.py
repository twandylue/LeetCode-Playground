class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """time complexity: O(n * m), space complexity: O(n * m), where n is the number of rows and m is the number of columns"""
        atlantic_set: set[tuple[int, int]] = set()
        pacific_set: set[tuple[int, int]] = set()
        for r in range(len(heights)):
            self.dfs(r, 0, pacific_set, heights[r][0], heights)
            self.dfs(r, len(heights[0]) - 1, atlantic_set, heights[r][-1], heights)
        for c in range(len(heights[0])):
            self.dfs(0, c, pacific_set, heights[0][c], heights)
            self.dfs(
                len(heights) - 1,
                c,
                atlantic_set,
                heights[-1][c],
                heights,
            )
        result: list[list[int]] = []
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    result.append([r, c])
        return result

    def dfs(
        self,
        r: int,
        c: int,
        visited: set[tuple[int, int]],
        pre_height: int,
        heights: list[list[int]],
    ) -> None:
        if (
            r < 0
            or r == len(heights)
            or c < 0
            or c == len(heights[r])
            or (r, c) in visited
            or pre_height > heights[r][c]
        ):
            return
        visited.add((r, c))
        self.dfs(r - 1, c, visited, heights[r][c], heights)
        self.dfs(r + 1, c, visited, heights[r][c], heights)
        self.dfs(r, c - 1, visited, heights[r][c], heights)
        self.dfs(r, c + 1, visited, heights[r][c], heights)


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


def test_pacificAtlantic_case_3():
    # arrange
    heights: list[list[int]] = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
    expected: list[list[int]] = [
        [0, 2],
        [0, 4],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 0],
    ]

    # act
    solution = Solution()
    actual = solution.pacificAtlantic(heights)

    # assert
    assert expected == actual
