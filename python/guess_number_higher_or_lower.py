# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l: int = 1
        r: int = n
        result: int = 0
        while l <= r:
            mid: int = (l + r) // 2
            result = mid
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1

        return result
