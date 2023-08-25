class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result: list[int] = digits[::-1]
        carry: int = 0
        result[0] += 1

        if result[0] // 10 > 0:
            carry = 1
            result[0] = result[0] % 10

        for i in range(1, len(result)):
            result[i] += carry
            carry = result[i] // 10
            if carry > 0:
                result[i] = result[i] % 10

        if carry > 0:
            result.append(1)

        return result[::-1]


def test_plusOne_case_1():
    # arrange
    input: list[int] = [1, 2, 3]
    expected: list[int] = [1, 2, 4]

    # act
    result = Solution().plusOne(input)

    # assert
    assert result == expected


def test_plusOne_case_2():
    # arrange
    input: list[int] = [4, 3, 2, 1]
    expected: list[int] = [4, 3, 2, 2]

    # act
    result = Solution().plusOne(input)

    # assert
    assert result == expected


def test_plusOne_case_3():
    # arrange
    input: list[int] = [0]
    expected: list[int] = [1]

    # act
    result = Solution().plusOne(input)

    # assert
    assert result == expected


def test_plusOne_case_4():
    # arrange
    input: list[int] = [9, 9, 9, 9]
    expected: list[int] = [1, 0, 0, 0, 0]

    # act
    result = Solution().plusOne(input)

    # assert
    assert result == expected
