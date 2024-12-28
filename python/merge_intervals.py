class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """time: O(n logn)"""
        intervals.sort()
        result: list[list[int]] = [intervals[0]]
        for start, end in intervals:
            last_end: int = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        return result


def test_insert_case_1():
    # arrange
    intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected: list[list[int]] = [[1, 6], [8, 10], [15, 18]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual


def test_insert_case_2():
    # arrange
    intervals: list[list[int]] = [[1, 4], [0, 4]]
    expected: list[list[int]] = [[0, 4]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual


def test_insert_case_3():
    # arrange
    intervals: list[list[int]] = [[1, 4], [0, 0]]
    expected: list[list[int]] = [[0, 0], [1, 4]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual
