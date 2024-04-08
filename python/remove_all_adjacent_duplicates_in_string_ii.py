class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """time complexity: O(n), space complexity: O(n)"""
        stack: list[tuple[str, int]] = list()
        for i in range(len(s)):
            count: int = 1
            if len(stack) > 0 and stack[-1][0] == s[i]:
                count += stack[-1][1]
            if count == k:
                while len(stack) > 0 and stack[-1][0] == s[i]:
                    stack.pop()
            else:
                stack.append((s[i], count))
        return "".join([s[0] for s in stack])


def test_removeDuplicates_case_1():
    # arrange
    s: str = "abcd"
    k: int = 2
    expected: str = "abcd"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s, k)

    # assert
    assert expected == actual


def test_removeDuplicates_case_2():
    # arrange
    s: str = "deeedbbcccbdaa"
    k: int = 3
    expected: str = "aa"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s, k)

    # assert
    assert expected == actual


def test_removeDuplicates_case_3():
    # arrange
    s: str = "pbbcggttciiippooaais"
    k: int = 2
    expected: str = "ps"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s, k)

    # assert
    assert expected == actual


def test_removeDuplicates_case_4():
    # arrange
    s: str = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
    k: int = 4
    expected: str = "ybth"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s, k)

    # assert
    assert expected == actual
