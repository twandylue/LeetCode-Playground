use std::collections::HashMap;

type StationName = String;
type EnterTime = i32;
type COUNT = i32;
type AverageTime = f64;

struct UndergroundSystem {
    passenger_map: HashMap<i32, (StationName, EnterTime)>,
    station_map: HashMap<(StationName, StationName), (AverageTime, COUNT)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {
    fn new() -> Self {
        UndergroundSystem {
            passenger_map: HashMap::new(),
            station_map: HashMap::new(),
        }
    }

    // NOTE: time complexity: O(1)
    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.passenger_map
            .entry(id)
            .and_modify(|_x| {})
            .or_insert((station_name, t));
    }

    // NOTE: time complexity: O(1)
    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        if let Some((prev_station_name, prev_time)) = self.passenger_map.remove(&id) {
            let diff_time: i32 = t - prev_time;
            self.station_map
                .entry((prev_station_name, station_name))
                .and_modify(|(average_time, count)| {
                    *average_time =
                        (*average_time * (*count as f64) + diff_time as f64) / (*count + 1) as f64;
                    *count += 1;
                })
                .or_insert((diff_time as f64, 1));
        }
    }

    // NOTE: time complexity: O(1)
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        if let Some((average_time, _)) = self.station_map.get(&(start_station, end_station)) {
            return *average_time;
        }

        unreachable!("Something goes wrong!");
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn underground_system_case_1() {
        // arrange
        let mut system = UndergroundSystem::new();

        // assert
        system.check_in(45, "Leyton".to_string(), 3);
        system.check_in(32, "Paradise".to_string(), 8);
        system.check_in(27, "Leyton".to_string(), 10);
        system.check_out(45, "Waterloo".to_string(), 15);
        system.check_out(27, "Waterloo".to_string(), 20);
        system.check_out(32, "Cambridge".to_string(), 22);
        assert_eq!(
            14.00000,
            system.get_average_time("Paradise".to_string(), "Cambridge".to_string())
        );
        assert_eq!(
            11.00000,
            system.get_average_time("Leyton".to_string(), "Waterloo".to_string())
        );
        system.check_in(10, "Leyton".to_string(), 24);
        assert_eq!(
            11.00000,
            system.get_average_time("Leyton".to_string(), "Waterloo".to_string())
        );
        system.check_out(10, "Waterloo".to_string(), 38);
        assert_eq!(
            12.00000,
            system.get_average_time("Leyton".to_string(), "Waterloo".to_string())
        );
    }
}
