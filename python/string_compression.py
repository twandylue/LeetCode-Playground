class Solution:
    def compress(self, chars: list[str]) -> int:
        l: int = 0
        r: int = 0
        while r < len(chars):
            count: int = 1
            while r < len(chars) - 1 and chars[r] == chars[r + 1]:
                count += 1
                r += 1

            chars[l] = chars[r]
            l += 1
            if count != 1:
                for n in str(count):
                    if l < len(chars):
                        chars[l] = n
                        l += 1
                    else:
                        break
            r += 1

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
