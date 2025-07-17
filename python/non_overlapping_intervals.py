class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """time complexity: O(n log n)"""
        count: int = 0
        end: float = -float("inf")
        intervals.sort(key=lambda x: x[1])

        for i in range(len(intervals)):
            if end > intervals[i][0]:
                count += 1
            else:
                end = intervals[i][1]

        return count

    def eraseOverlapIntervals2(self, intervals: list[list[int]]) -> int:
        """time complexity: O(n log n)"""
        result: int = 0
        intervals.sort()
        curr_e: int = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= curr_e:
                curr_e = end
            else:
                curr_e = min(curr_e, end)
                result += 1
        return result


def test_eraseOverlapIntervals_case_1():
    # arrange
    intervals: list[list[int]] = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.eraseOverlapIntervals(intervals)

    # assert
    assert expected == actual


def test_eraseOverlapIntervals_case_2():
    # arrange
    intervals: list[list[int]] = [[1, 2], [1, 2], [1, 2]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.eraseOverlapIntervals(intervals)

    # assert
    assert expected == actual


def test_eraseOverlapIntervals_case_3():
    # arrange
    intervals: list[list[int]] = [[1, 2], [2, 3]]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.eraseOverlapIntervals(intervals)

    # assert
    assert expected == actual


def test_eraseOverlapIntervals_case_3():
    # arrange
    intervals: list[list[int]] = [[1, 100], [11, 22], [1, 11], [2, 12]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.eraseOverlapIntervals(intervals)

    # assert
    assert expected == actual
