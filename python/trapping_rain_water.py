class Solution:
    def trap(self, height: list[int]) -> int:
        output = 0
        max_lefts: list[int] = []
        max_rights: list[int] = []

        for i in range(len(height)):
            if i == 0:
                max_lefts.append(height[i])
            val: int = max(max_lefts[-1], height[i])
            max_lefts.append(val)

        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                max_rights.append(height[i])
            val: int = max(max_rights[-1], height[i])
            max_rights.append(val)
        new_max_rights = list(reversed(max_rights))

        for i in range(len(height)):
            val: int = min(max_lefts[i], new_max_rights[i]) - height[i]
            if val > 0:
                output += val
            else:
                continue

        return output

    def trap_2(self, height: list[int]) -> int:
        output: int = 0
        max_left: int = height[0]
        max_right: int = height[-1]
        l: int = 0
        r: int = len(height) - 1
        while l < r and l < len(height) and r > 0:
            if height[l] <= height[r]:
                max_left = max(max_left, height[l])
                if max_left - height[l] > 0:
                    output += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                if max_right - height[r] > 0:
                    output += max_right - height[r]
                r -= 1

        return output


def test_trap_case_1():
    # arrange
    height: list[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.trap(height)

    # assert
    assert actual == expected


def test_trap_case_2():
    # arrange
    height: list[int] = [4, 2, 0, 3, 2, 5]
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.trap(height)

    # assert
    assert actual == expected


def test_trap_case_3():
    # arrange
    height: list[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.trap_2(height)

    # assert
    assert actual == expected


def test_trap_case_4():
    # arrange
    height: list[int] = [4, 2, 0, 3, 2, 5]
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.trap_2(height)

    # assert
    assert actual == expected
