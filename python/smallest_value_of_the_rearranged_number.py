class Solution:
    def smallestNumber(self, num: int) -> int:
        num_str: str = str(num)
        num_strs: list[str] = [""] * len(num_str)
        for i in range(len(num_str)):
            num_strs[i] = num_str[i]

        if num > 0:
            num_strs.sort()
            last_zero_index: int = 0
            for i in range(len(num_strs)):
                if num_strs[i] == "0":
                    continue
                last_zero_index = i
                break
            tmp: str = num_strs[last_zero_index]
            num_strs[last_zero_index] = "0"
            num_strs[0] = tmp
            return int("".join(num_strs))

        num_parts = num_strs[1::]
        num_parts.sort(reverse=True)
        return int(num_strs[0] + "".join(num_parts))


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
