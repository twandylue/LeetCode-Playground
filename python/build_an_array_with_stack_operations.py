class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        """time complexity: O(n)"""
        stack: list[int] = []
        result: list[str] = []
        idx: int = 0
        for i in range(1, n + 1):
            if idx >= len(target) or stack == target:
                break
            if i == target[idx]:
                stack.append(i)
                result.append("Push")
                idx += 1
            else:
                result.append("Push")
                result.append("Pop")
        return result


def test_buildArray_case_1():
    # arrange
    target: list[int] = [1, 3]
    n: int = 3
    expected: list[str] = ["Push", "Push", "Pop", "Push"]

    # act
    actual = Solution().buildArray(target, n)

    # assert
    assert expected == actual


def test_buildArray_case_2():
    # arrange
    target: list[int] = [1, 2, 3]
    n: int = 3
    expected: list[str] = ["Push", "Push", "Push"]

    # act
    actual = Solution().buildArray(target, n)

    # assert
    assert expected == actual


def test_buildArray_case_3():
    # arrange
    target: list[int] = [1, 2]
    n: int = 4
    expected: list[str] = ["Push", "Push"]

    # act
    actual = Solution().buildArray(target, n)

    # assert
    assert expected == actual
