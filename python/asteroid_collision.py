class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """time complexity: O(n), space complexity: O(n)"""
        stack: list[int] = []
        i: int = 0
        while i < len(asteroids):
            if (
                len(stack) > 0
                and stack[-1] * asteroids[i] < 0
                and stack[-1] >= asteroids[i]
            ):
                if stack[-1] + asteroids[i] > 0:
                    i += 1
                elif stack[-1] + asteroids[i] == 0:
                    stack.pop()
                    i += 1
                else:
                    stack.pop()
            else:
                stack.append(asteroids[i])
                i += 1
        return stack

    def asteroidCollision2(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = list()

        for i in range(len(asteroids)):
            flag: bool = True
            while len(stack) > 0 and stack[-1] * asteroids[i] < 0:
                if stack[-1] > 0:
                    if stack[-1] + asteroids[i] > 0:
                        flag = False
                        break
                    elif stack[-1] + asteroids[i] < 0:
                        stack.pop()
                    else:
                        flag = False
                        stack.pop()
                        break
                else:
                    flag = True
                    break

            if flag:
                stack.append(asteroids[i])

        return stack


def test_asteroidCollision_case_1():
    # arrange
    asteroids: list[int] = [5, 10, -5]
    expected: list[int] = [5, 10]

    # act
    solution = Solution()
    actual = solution.asteroidCollision(asteroids)

    # assert
    assert expected == actual


def test_asteroidCollision_case_2():
    # arrange
    asteroids: list[int] = [8, -8]
    expected: list[int] = []

    # act
    solution = Solution()
    actual = solution.asteroidCollision(asteroids)

    # assert
    assert expected == actual


def test_asteroidCollision_case_3():
    # arrange
    asteroids: list[int] = [10, 2, -5]
    expected: list[int] = [10]

    # act
    solution = Solution()
    actual = solution.asteroidCollision(asteroids)

    # assert
    assert expected == actual


def test_asteroidCollision_case_4():
    # arrange
    asteroids: list[int] = [-4, 6]
    expected: list[int] = [-4, 6]

    # act
    solution = Solution()
    actual = solution.asteroidCollision(asteroids)

    # assert
    assert expected == actual
