class UndergroundSystem:
    def __init__(self):
        self.passenger_table: dict[int, tuple[str, int]] = dict()
        self.station_table: dict[tuple[str, str], tuple[float, int]] = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_table[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.passenger_table.pop(id)
        diffTime: int = t - time
        if (startStation, stationName) in self.station_table:
            averageTime, count = self.station_table[(startStation, stationName)]
            self.station_table[(startStation, stationName)] = (
                float(averageTime * count + diffTime) / (count + 1),
                count + 1,
            )
        else:
            self.station_table[(startStation, stationName)] = (diffTime, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.station_table:
            return round(self.station_table[(startStation, endStation)][0], 5)

        return 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
def test_UndergroundSystem_case_1():
    system = UndergroundSystem()
    system.checkIn(45, "Leyton", 3)
    system.checkIn(32, "Paradise", 8)
    system.checkIn(27, "Leyton", 10)
    system.checkOut(45, "Waterloo", 15)
    system.checkOut(27, "Waterloo", 20)
    system.checkOut(32, "Cambridge", 22)
    assert 14.00000 == system.getAverageTime("Paradise", "Cambridge")
    assert 11.00000 == system.getAverageTime("Leyton", "Waterloo")
    system.checkIn(10, "Leyton", 24)
    assert 11.00000 == system.getAverageTime("Leyton", "Waterloo")
    system.checkOut(10, "Waterloo", 38)
    assert 12.00000 == system.getAverageTime("Leyton", "Waterloo")


def test_UndergroundSystem_case_2():
    system = UndergroundSystem()
    system.checkIn(10, "Leyton", 3)
    system.checkOut(10, "Paradise", 8)
    assert 5.00000 == system.getAverageTime("Leyton", "Paradise")
    system.checkIn(5, "Leyton", 10)
    system.checkOut(5, "Paradise", 16)
    assert 5.50000 == system.getAverageTime("Leyton", "Paradise")
    system.checkIn(2, "Leyton", 21)
    system.checkOut(2, "Paradise", 30)
    assert 6.66667 == system.getAverageTime("Leyton", "Paradise")
