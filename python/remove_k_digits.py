class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: list[str] = list()
        for i in range(len(num)):
            while len(stack) > 0 and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1

        p: int = 0
        for i in range(len(stack)):
            if stack[i] == "0":
                p += 1
            elif stack[i] != "0":
                break
        result: str = "".join(stack[p::])

        return "0" if len(result) == 0 else result


def test_removeKdigits_case_1():
    # arrange
    num: str = "1432219"
    k: int = 3
    expected: str = "1219"

    # act
    solution = Solution()
    actual = solution.removeKdigits(num, k)

    # assert
    assert expected == actual


def test_removeKdigits_case_2():
    # arrange
    num: str = "10200"
    k: int = 1
    expected: str = "200"

    # act
    solution = Solution()
    actual = solution.removeKdigits(num, k)

    # assert
    assert expected == actual


def test_removeKdigits_case_3():
    # arrange
    num: str = "10"
    k: int = 2
    expected: str = "0"

    # act
    solution = Solution()
    actual = solution.removeKdigits(num, k)

    # assert
    assert expected == actual


def test_removeKdigits_case_4():
    # arrange
    num: str = "9"
    k: int = 1
    expected: str = "0"

    # act
    solution = Solution()
    actual = solution.removeKdigits(num, k)

    # assert
    assert expected == actual


def test_removeKdigits_case_5():
    # arrange
    num: str = "10001"
    k: int = 4
    expected: str = "0"

    # act
    solution = Solution()
    actual = solution.removeKdigits(num, k)

    # assert
    assert expected == actual
