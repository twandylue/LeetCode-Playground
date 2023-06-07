struct Solution {}

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut output: i32 = 0;
        let mut current: f64 = 0.0;

        let mut cars: Vec<(i32, f64)> = std::iter::zip(position, speed)
            .map(|(p, s)| (p, ((target - p) / s) as f64))
            .collect();
        cars.sort_by(|a, b| b.0.cmp(&a.0));

        for (_, time) in cars {
            if time > current {
                current = time;
                output += 1;
            }
        }

        return output;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn car_fleet_case_1() {
        // arrange
        let target = 12;
        let position = vec![10, 8, 0, 5, 3];
        let speed = vec![2, 4, 1, 1, 3];
        let expected = 3;

        // act
        let actual = Solution::car_fleet(target, position, speed);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn car_fleet_case_2() {
        // arrange
        let target = 10;
        let position = vec![3];
        let speed = vec![3];
        let expected = 1;

        // act
        let actual = Solution::car_fleet(target, position, speed);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn car_fleet_case_3() {
        // arrange
        let target = 100;
        let position = vec![0, 2, 4];
        let speed = vec![4, 2, 1];
        let expected = 1;

        // act
        let actual = Solution::car_fleet(target, position, speed);

        // arrange
        assert_eq!(expected, actual);
    }
}
