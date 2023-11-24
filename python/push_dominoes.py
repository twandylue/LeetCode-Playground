from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        que: deque[tuple[int, str]] = deque()
        dominoes: list[str] = list(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] != ".":
                que.append((i, dominoes[i]))
        while len(que) > 0:
            i, d = que.popleft()
            if d == "L" and i > 0 and dominoes[i - 1] == ".":
                dominoes[i - 1] = "L"
                que.append((i - 1, "L"))
            if d == "R" and i < len(dominoes) - 1 and dominoes[i + 1] == ".":
                if i < len(dominoes) - 2 and dominoes[i + 2] == "L":
                    que.popleft()
                else:
                    dominoes[i + 1] = "R"
                    que.append((i + 1, "R"))

        return "".join(dominoes)


def test_pushDominoes_case_1():
    # arrange
    dominoes: str = "RR.L"
    expected: str = "RR.L"

    # act
    solution = Solution()
    actual = solution.pushDominoes(dominoes)

    # assert
    assert expected == actual


def test_pushDominoes_case_2():
    # arrange
    dominoes: str = ".L.R...LR..L.."
    expected: str = "LL.RR.LLRRLL.."

    # act
    solution = Solution()
    actual = solution.pushDominoes(dominoes)

    # assert
    assert expected == actual
