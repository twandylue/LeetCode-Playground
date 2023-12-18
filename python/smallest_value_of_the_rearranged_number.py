class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        numStrs: list[str] = list(str(num))
        if num > 0:
            numStrs.sort()
            if numStrs[0] == "0":
                firstNonZeroIndex: int = 0
                for i in range(len(numStrs)):
                    if numStrs[i] == "0":
                        continue
                    firstNonZeroIndex = i
                    break
                tmp: int = numStrs[firstNonZeroIndex]
                numStrs[firstNonZeroIndex] = numStrs[0]
                numStrs[0] = tmp
            return int("".join(numStrs))

        numParts = numStrs[1::]
        numParts.sort(reverse=True)
        return int("-" + "".join(numParts))


def test_smallestNumber_case_1():
    # arrange
    num: int = 310
    expected: int = 103

    # act
    solution = Solution()
    actual = solution.smallestNumber(num)

    # assert
    assert expected == actual


def test_smallestNumber_case_2():
    # arrange
    num: int = -7605
    expected: int = -7650

    # act
    solution = Solution()
    actual = solution.smallestNumber(num)

    # assert
    assert expected == actual
