class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result: set[tuple[char, char]] = set()
        left: set[char] = set()
        right: dict[char, i32] = dict()

        for c in s:
            if c not in right:
                right[c] = 1
            else:
                right[c] += 1

        for i in range(len(s)):
            if s[i] in right:
                right[s[i]] -= 1
            if right[s[i]] <= 0:
                right.pop(s[i])

            for j in range(0, 26):
                leftChar: char = chr(ord("a") + j)
                if leftChar in left and leftChar in right:
                    result.add((s[i], leftChar))
            left.add(s[i])

        return len(result)


def test_countPalindromicSubsequence_case_1():
    # arrange
    s: str = "aabca"
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.countPalindromicSubsequence(s)

    # assert
    assert actual == expected


def test_countPalindromicSubsequence_case_2():
    # arrange
    s: str = "adc"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.countPalindromicSubsequence(s)

    # assert
    assert actual == expected
