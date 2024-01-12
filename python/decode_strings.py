class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[str] = list()
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                accu: str = ""
                while len(stack) > 0 and stack[-1] != "[":
                    accu = stack.pop() + accu
                stack.pop()
                times: str = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    times = stack.pop() + times
                times: int = int(times)
                accu = accu * times
                stack.append(accu)

        return "".join(stack)


def test_decodeString_case_1():
    # arrange
    s: str = "3[a]2[bc]"
    expected: str = "aaabcbc"

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual


def test_decodeString_case_2():
    # arrange
    s: str = "3[a2[c]]"
    expected: str = "accaccacc"

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual


def test_decodeString_case_3():
    # arrange
    s: str = "2[abc]3[cd]ef"
    expected: str = "abcabccdcdcdef"

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual


def test_decodeString_case_4():
    # arrange
    s: str = "abc3[cd]xyz"
    expected: str = "abccdcdcdxyz"

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual


def test_decodeString_case_5():
    # arrange
    s: str = "100[leetcode]"
    expected: str = "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual
