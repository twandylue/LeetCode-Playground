class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        result: liet[int] = self.divide_and_merge(nums)

        return result

    def divide_and_merge(self, nums: list[int]) -> list[int]:
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return [nums[0], nums[1]]
            else:
                return [nums[1], nums[0]]
        if len(nums) == 1:
            return [nums[0]]

        mid: int = int((len(nums) + 1) / 2)
        leftNums: list[int] = self.divide_and_merge(nums[:mid])
        rightNums: list[int] = self.divide_and_merge(nums[mid:])

        return self.merge(leftNums, rightNums)

    def merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m: int = len(nums1)
        n: int = len(nums2)
        index: int = m + n - 1
        afterNums: list[int] = [0] * (m + n)

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                afterNums[index] = nums1[m - 1]
                m -= 1
            else:
                afterNums[index] = nums2[n - 1]
                n -= 1
            if index > 0:
                index -= 1

        while m > 0 or n > 0:
            if m > 0:
                afterNums[index] = nums1[m - 1]
                m -= 1
            if n > 0:
                afterNums[index] = nums2[n - 1]
                n -= 1
            if index > 0:
                index -= 1

        return afterNums


def test_sort_an_array_case_1():
    # arrange
    numbers: list[int] = [5, 2, 3, 1]
    expected: list[int] = [1, 2, 3, 5]

    # act
    solution = Solution()
    actual: list[int] = solution.sortArray(numbers)

    # assert
    assert actual == expected


def test_sort_an_array_case_2():
    # arrange
    numbers: list[int] = [5, 1, 1, 2, 0, 0]
    expected: list[int] = [0, 0, 1, 1, 2, 5]

    # act
    solution = Solution()
    actual: list[int] = solution.sortArray(numbers)

    # assert
    assert actual == expected


def test_sort_an_array_case_3():
    # arrange
    numbers: list[int] = [
        -74,
        48,
        -20,
        2,
        10,
        -84,
        -5,
        -9,
        11,
        -24,
        -91,
        2,
        -71,
        64,
        63,
        80,
        28,
        -30,
        -58,
        -11,
        -44,
        -87,
        -22,
        54,
        -74,
        -10,
        -55,
        -28,
        -46,
        29,
        10,
        50,
        -72,
        34,
        26,
        25,
        8,
        51,
        13,
        30,
        35,
        -8,
        50,
        65,
        -6,
        16,
        -2,
        21,
        -78,
        35,
        -13,
        14,
        23,
        -3,
        26,
        -90,
        86,
        25,
        -56,
        91,
        -13,
        92,
        -25,
        37,
        57,
        -20,
        -69,
        98,
        95,
        45,
        47,
        29,
        86,
        -28,
        73,
        -44,
        -46,
        65,
        -84,
        -96,
        -24,
        -12,
        72,
        -68,
        93,
        57,
        92,
        52,
        -45,
        -2,
        85,
        -63,
        56,
        55,
        12,
        -85,
        77,
        -39,
    ]
    expected: list[int] = [
        -96,
        -91,
        -90,
        -87,
        -85,
        -84,
        -84,
        -78,
        -74,
        -74,
        -72,
        -71,
        -69,
        -68,
        -63,
        -58,
        -56,
        -55,
        -46,
        -46,
        -45,
        -44,
        -44,
        -39,
        -30,
        -28,
        -28,
        -25,
        -24,
        -24,
        -22,
        -20,
        -20,
        -13,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -6,
        -5,
        -3,
        -2,
        -2,
        2,
        2,
        8,
        10,
        10,
        11,
        12,
        13,
        14,
        16,
        21,
        23,
        25,
        25,
        26,
        26,
        28,
        29,
        29,
        30,
        34,
        35,
        35,
        37,
        45,
        47,
        48,
        50,
        50,
        51,
        52,
        54,
        55,
        56,
        57,
        57,
        63,
        64,
        65,
        65,
        72,
        73,
        77,
        80,
        85,
        86,
        86,
        91,
        92,
        92,
        93,
        95,
        98,
    ]

    # act
    solution = Solution()
    actual: list[int] = solution.sortArray(numbers)

    # assert
    assert actual == expected
