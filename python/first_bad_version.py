# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(mid: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l: int = 1
        r: int = n
        while l < r:
            mid: int = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
