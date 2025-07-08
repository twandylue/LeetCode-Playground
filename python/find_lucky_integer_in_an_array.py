from collections import defaultdict


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counter: dict[int, int] = defaultdict(int)
        for num in arr:
            counter[num] += 1
        result: int = -1
        for k, v in counter.items():
            if k == v:
                result = max(k, result)
        return result if result != -1 else -1


def test_findLuchk_case_1():
    # arrange
    arr: list[int] = [1, 2, 2, 3, 3, 3]
    expected: int = 3

    # act
    actual = Solution().findLucky(arr)

    # assert
    assert expected == actual


def test_findLuchk_case_2():
    # arrange
    arr: list[int] = [2, 2, 2, 3, 3]
    expected: int = -1

    # act
    actual = Solution().findLucky(arr)

    # assert
    assert expected == actual
