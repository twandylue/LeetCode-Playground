class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        center: int = self.binarySearch(arr, x)
        if k == 1:
            return [arr[center]]
        if center == 0:
            return arr[:k]
        if center == len(arr) - 1:
            return arr[len(arr) - k :]

        l: int = center
        r: int = center
        while l >= 0 and r < len(arr):
            if r - l + 1 == k:
                return arr[l : r + 1]
            if l == 0:
                r += 1
                continue
            if r == len(arr) - 1:
                l -= 1
                continue

            if x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:
                r += 1

        return arr[l : r + 1]

    def binarySearch(self, arr: list[int], target: int) -> int:
        if target < arr[0]:
            return 0
        if target > arr[-1]:
            return len(arr) - 1

        l: int = 0
        r: int = len(arr) - 1
        mid: int = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > target:
                if mid > 0 and target > arr[mid - 1]:
                    return self.getClosest(arr, mid - 1, mid, target)
                r = mid - 1
            elif arr[mid] < target:
                if mid < len(arr) - 1 and target < arr[mid + 1]:
                    return self.getClosest(arr, mid, mid + 1, target)
                l = mid + 1
            else:
                return mid

        return mid

    def getClosest(self, arr: list[int], pos1: int, pos2: int, target: int) -> int:
        if target - arr[pos1] > arr[pos2] - target:
            return pos2
        return pos1


def test_findClosestElements_case_1():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    k: int = 4
    x: int = 3
    expected: list[int] = [1, 2, 3, 4]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_2():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    k: int = 4
    x: int = -1
    expected: list[int] = [1, 2, 3, 4]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_3():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    k: int = 4
    x: int = 6
    expected: list[int] = [2, 3, 4, 5]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_4():
    # arrange
    arr: list[int] = [1, 1, 1, 10, 10, 10]
    k: int = 1
    x: int = 9
    expected: list[int] = [10]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_5():
    # arrange
    arr: list[int] = [1, 2, 3, 4, 5]
    k: int = 4
    x: int = 4
    expected: list[int] = [2, 3, 4, 5]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_6():
    # arrange
    arr: list[int] = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
    k: int = 9
    x: int = 4
    expected: list[int] = [0, 1, 1, 1, 2, 3, 6, 7, 8]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_7():
    # arrange
    arr: list[int] = [-2, -1, 1, 2, 3, 4, 5]
    k: int = 7
    x: int = 3
    expected: list[int] = [-2, -1, 1, 2, 3, 4, 5]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_8():
    # arrange
    arr: list[int] = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k: int = 3
    x: int = 5
    expected: list[int] = [3, 3, 4]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual


def test_findClosestElements_case_9():
    # arrange
    arr: list[int] = [0, 0, 0, 1, 3, 5, 6, 7, 8, 8]
    k: int = 2
    x: int = 2
    expected: list[int] = [1, 3]

    # act
    solution = Solution()
    actual = solution.findClosestElements(arr, k, x)

    # assert
    assert expected == actual
