class Solution:
    # NOTE: time complexity: O(n)
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        result: int = 0
        l: int = 0
        r: int = 0
        accu: int = 0
        while r < len(arr):
            accu += arr[r]
            if r - l + 1 > k:
                accu -= arr[l]
                l += 1
            if r - l + 1 == k and accu / (r - l + 1) >= threshold:
                result += 1

            r += 1

        return result


def test_numOfSubarrays_case_1():
    # arrange
    arr: list[int] = [2, 2, 2, 2, 5, 5, 5, 8]
    k: int = 3
    threshold: int = 4
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.numOfSubarrays(arr, k, threshold)

    # assert
    assert expected == actual


def test_numOfSubarrays_case_2():
    # arrange
    arr: list[int] = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k: int = 3
    threshold: int = 5
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.numOfSubarrays(arr, k, threshold)

    # assert
    assert expected == actual
