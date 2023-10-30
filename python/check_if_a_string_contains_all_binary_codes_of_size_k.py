class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combSet: set[str] = set()
        for i in range(0, len(s) - k + 1):
            a = s[i : i + k]
            combSet.add(s[i : i + k])

        return len(combSet) == pow(2, k)


def test_hasAllCodes_case_1():
    # arrange
    s: str = "00110110"
    k: int = 2
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasAllCodes(s, k)

    # assert
    assert expected == actual


def test_hasAllCodes_case_2():
    # arrange
    s: str = "0110"
    k: int = 1
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasAllCodes(s, k)

    # assert
    assert expected == actual


def test_hasAllCodes_case_3():
    # arrange
    s: str = "0110"
    k: int = 2
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.hasAllCodes(s, k)

    # assert
    assert expected == actual


def test_hasAllCodes_case_4():
    # arrange
    s: str = "00110"
    k: int = 2
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.hasAllCodes(s, k)

    # assert
    assert expected == actual
