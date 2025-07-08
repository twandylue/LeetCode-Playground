class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        result: int = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime and queryTime <= e:
                result += 1
        return result


def test_busyStudent_case_1():
    # arrange
    startTime: list[int] = [1, 2, 3]
    endTime: list[int] = [3, 2, 7]
    queryTime: int = 4
    expected: int = 1

    # act
    actual: int = Solution().busyStudent(startTime, endTime, queryTime)

    # assert
    assert expected == actual


def test_busyStudent_case_2():
    # arrange
    startTime: list[int] = [4]
    endTime: list[int] = [4]
    queryTime: int = 4
    expected: int = 1

    # act
    actual: int = Solution().busyStudent(startTime, endTime, queryTime)

    # assert
    assert expected == actual
