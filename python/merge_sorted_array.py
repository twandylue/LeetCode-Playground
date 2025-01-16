class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i: int = m - 1
        j: int = n - 1
        k: int = len(nums1) - 1
        while k >= 0 and (i >= 0 or j >= 0):
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif i >= 0:
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


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
