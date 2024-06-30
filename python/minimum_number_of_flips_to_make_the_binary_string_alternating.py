class Solution:
    def minFlips(self, s: str) -> int:
        result: int = float("inf")
        n: int = len(s)
        s = s + s
        target1: str = ""
        target2: str = ""
        for i in range(len(s)):
            if i % 2 == 0:
                target1 += "0"
                target2 += "1"
            else:
                target1 += "1"
                target2 += "0"
        diff1: int = 0
        diff2: int = 0
        l: int = 0
        for r in range(len(s)):
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1

            if r - l + 1 > n:
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
            if r - l + 1 == n:
                result = min(result, diff1, diff2)

        return result


def test_minFlips_case_1():
    # arrange
    s: str = "111000"
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minFlips(s)

    # assert
    assert expected == actual


def test_minFlips_case_2():
    # arrange
    s: str = "010"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minFlips(s)

    # assert
    assert expected == actual


def test_minFlips_case_3():
    # arrange
    s: str = "1110"
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minFlips(s)

    # assert
    assert expected == actual
