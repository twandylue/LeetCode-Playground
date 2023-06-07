class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        output: int = 0
        curr: float = 0.0
        cars: list[tuple[int, int]] = list(zip(position, speed))
        sortCars: list[tuple[int, float]] = list(
            map(lambda x: (x[0], (target - x[0]) / x[1]), cars)
        )
        sortCars.sort(key=lambda x: x[0], reverse=True)

        for _, time in sortCars:
            if time > curr:
                curr = time
                output += 1

        return output

    def carFleet2(self, target: int, position: list[int], speed: list[int]) -> int:
        stack: list[float] = []
        cars: list[tuple[int, int]] = list(zip(position, speed))
        sortCars: list[tuple[int, float]] = list(
            map(lambda x: (x[0], (target - x[0]) / x[1]), cars)
        )
        sortCars.sort(key=lambda x: x[0])

        for _, time in sortCars:
            while len(stack) > 0 and time >= stack[-1]:
                stack.pop()

            stack.append(time)

        return len(stack)


def test_car_fleet_case_1():
    # arrange
    target: int = 12
    position: list[int] = [10, 8, 0, 5, 3]
    speed: list[int] = [2, 4, 1, 1, 3]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.carFleet(target, position, speed)

    # assert
    assert expected == actual


def test_car_fleet_case_2():
    # arrange
    target: int = 10
    position: list[int] = [3]
    speed: list[int] = [3]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.carFleet(target, position, speed)

    # assert
    assert expected == actual


def test_car_fleet_case_3():
    # arrange
    target: int = 100
    position: list[int] = [0, 2, 4]
    speed: list[int] = [4, 2, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.carFleet(target, position, speed)

    # assert
    assert expected == actual


def test_car_fleet2_case_1():
    # arrange
    target: int = 12
    position: list[int] = [10, 8, 0, 5, 3]
    speed: list[int] = [2, 4, 1, 1, 3]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.carFleet2(target, position, speed)

    # assert
    assert expected == actual


def test_car_fleet2_case_2():
    # arrange
    target: int = 10
    position: list[int] = [3]
    speed: list[int] = [3]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.carFleet2(target, position, speed)

    # assert
    assert expected == actual


def test_car_fleet2_case_3():
    # arrange
    target: int = 100
    position: list[int] = [0, 2, 4]
    speed: list[int] = [4, 2, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.carFleet2(target, position, speed)

    # assert
    assert expected == actual
