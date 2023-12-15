class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_num = big
        self.med_num = medium
        self.small_num = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_num > 0:
            self.big_num -= 1
            return True
        if carType == 2 and self.med_num > 0:
            self.med_num -= 1
            return True
        if carType == 3 and self.small_num > 0:
            self.small_num -= 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
def test_ParkingSystem_case1():
    p = ParkingSystem(1, 1, 0)
    assert p.addCar(1)
    assert p.addCar(2)
    assert not p.addCar(3)
    assert not p.addCar(1)
