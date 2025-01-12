class Solution:
    def simplifyPath(self, path: str) -> str:
        """time complexity: O(n)"""
        stack: list[str] = []
        path += "/"
        curr: str = ""
        for c in path:
            if c == "/":
                if curr == ".." and len(stack) > 0:
                    stack.pop()
                if curr != "." and curr != ".." and curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)


def test_simplifyPath_case_1():
    # arrange
    path: str = "/home/"
    expected: str = "/home"

    # act
    solution = Solution()
    actual = solution.simplifyPath(path)

    # assert
    assert expected == actual


def test_simplifyPath_case_2():
    # arrange
    path: str = "/../"
    expected: str = "/"

    # act
    solution = Solution()
    actual = solution.simplifyPath(path)

    # assert
    assert expected == actual


def test_simplifyPath_case_3():
    # arrange
    path: str = "/home//foo/"
    expected: str = "/home/foo"

    # act
    solution = Solution()
    actual = solution.simplifyPath(path)

    # assert
    assert expected == actual


def test_simplifyPath_case_4():
    # arrange
    path: str = "/home/user/Documents/../Pictures"
    expected: str = "/home/user/Pictures"

    # act
    solution = Solution()
    actual = solution.simplifyPath(path)

    # assert
    assert expected == actual
