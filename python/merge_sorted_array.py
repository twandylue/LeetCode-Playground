class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last: int = len(nums1) - 1
        r1: int = m - 1
        r2: int = n - 1

        while r1 >= 0 and r2 >= 0 and last >= 0:
            if nums1[r1] > nums2[r2]:
                nums1[last] = nums1[r1]
                r1 -= 1
            else:
                nums1[last] = nums2[r2]
                r2 -= 1
            last -= 1

        while r1 >= 0 and last >= 0:
            nums1[last] = nums1[r1]
            r1 -= 1
            last -= 1

        while r2 >= 0 and last >= 0:
            nums1[last] = nums2[r2]
            r2 -= 1
            last -= 1


def test_merge_sorted_array_case_1():
    # arrange
    nums1: list[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    nums2: list[int] = [2, 5, 6]
    n: int = 3
    expected: list[int] = [1, 2, 2, 3, 5, 6]

    # act
    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    # assert
    assert nums1 == expected


def test_merge_sorted_array_case_2():
    # arrange
    nums1: list[int] = [1]
    m: int = 1
    nums2: list[int] = []
    n: int = 0
    expected: list[int] = [1]

    # act
    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    # assert
    assert nums1 == expected


def test_merge_sorted_array_case_3():
    # arrange
    nums1: list[int] = [0]
    m: int = 0
    nums2: list[int] = [1]
    n: int = 1
    expected: list[int] = [1]

    # act
    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    # assert
    assert nums1 == expected
