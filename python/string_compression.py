class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1

        result: int = 0
        prev: str = chars[0]
        count: int = 0
        l: int = 0
        r: int = 0
        while l <= r and r < len(chars):
            if chars[r] == prev:
                r += 1
                count += 1
                continue

            countStr: str = str(count)
            count = 0
            chars[l] = prev
            prev = chars[r]
            l += 1
            if countStr == "1":
                continue
            for c in countStr:
                chars[l] = c
                l += 1
            print(chars)

        if count == 1:
            chars[l] = prev
            return l + 1

        if r == len(chars) and chars[r - 1] == prev:
            countStr: str = str(count)
            chars[l] = prev
            l += 1
            for c in countStr:
                chars[l] = c
                l += 1

        return l


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
