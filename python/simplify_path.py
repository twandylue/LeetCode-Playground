class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: list[str] = list()
        path += "/"
        curr: str = ""
        for i in range(len(path)):
            if path[i] == "/":
                if curr == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif curr != "." and curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr += path[i]

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
