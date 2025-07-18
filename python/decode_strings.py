class Solution:
    def decodeString(self, s: str) -> str:
        """time complexity: O(n^2)"""
        stack: list[str] = list()
        for i in range(len(s)):
            if s[i] == "]":
                accu: str = ""
                while len(stack) > 0 and stack[-1] != "[":
                    accu = stack.pop() + accu
                stack.pop()
                times: str = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    times = stack.pop() + times
                k: int = int(times)
                stack.append(accu * k)
            else:
                stack.append(s[i])

        return "".join(stack)

    def decodeString2(self, s: str) -> str:
        """time complexity: O(n)"""
        _, result = self.helper(0, s)
        return result

    def helper(self, i: int, s: str) -> tuple[int, str]:
        num: int = 0
        result: str = ""
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                i, subs = self.helper(i + 1, s)
                result = result + num * subs
                num = 0
            elif s[i] == "]":
                return i, result
            else:
                result += s[i]
            i += 1
        return i, result


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
    expected: str = (
        "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
    )

    # act
    solution = Solution()
    actual = solution.decodeString(s)

    # assert
    assert expected == actual


def test_decodeString_case_6():
    # arrange
    s: str = "100[leetcode]"
    expected: str = (
        "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
    )

    # act
    solution = Solution()
    actual = solution.decodeString2(s)

    # assert
    assert expected == actual


def test_decodeString_case_7():
    # arrange
    s: str = "3[a]2[bc]"
    expected: str = "aaabcbc"

    # act
    solution = Solution()
    actual = solution.decodeString2(s)

    # assert
    assert expected == actual
