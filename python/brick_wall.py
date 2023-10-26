class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        count: int = 0
        wallDict: dict[int, int] = dict()
        width: int = 0
        for i in range(len(wall)):
            accu: int = 0
            for j in range(len(wall[i])):
                accu += wall[i][j]
                if accu not in wallDict:
                    wallDict[accu] = 1
                else:
                    wallDict[accu] += 1
            width = accu

        for k, v in wallDict.items():
            if k == width:
                continue
            count = max(count, v)

        return len(wall) - count


def test_leastBricks_case_1():
    # arrange
    wall: list[list[int]] = [
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1],
    ]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.leastBricks(wall)

    # assert
    assert expected == actual


def test_leastBricks_case_2():
    # arrange
    wall: list[list[int]] = [[1], [1], [1]]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.leastBricks(wall)

    # assert
    assert expected == actual


def test_leastBricks_case_3():
    # arrange
    wall: list[list[int]] = [[2], [2], [1, 1]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.leastBricks(wall)

    # assert
    assert expected == actual
