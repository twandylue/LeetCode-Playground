class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1
        l: int = 0
        r: int = 1
        curr: int = 0

        while r < len(chars):
            while r < len(chars) and chars[r] == chars[l]:
                r += 1

            chars[curr] = chars[l]
            curr += 1
            count: str = str(r - l)
            if count == "1":
                l = r
                continue
            for c in count:
                chars[curr] = c
                curr += 1
            l = r

        return curr


def test_compress_case_1():
    # arrange
    chars: list[str] = ["a", "a", "b", "b", "c", "c", "c"]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual


def test_compress_case_2():
    # arrange
    chars: list[str] = ["a"]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual


def test_compress_case_3():
    # arrange
    chars: list[str] = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual


def test_compress_case_4():
    # arrange
    chars: list[str] = ["a", "a", "a", "b", "b", "a", "a"]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual


def test_compress_case_5():
    # arrange
    chars: list[str] = ["a", "b", "c"]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual


def test_compress_case_6():
    # arrange
    chars: list[str] = ["a", "a", "a", "a", "a", "b"]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.compress(chars)

    # assert
    assert expected == actual
