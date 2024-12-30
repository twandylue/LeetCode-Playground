use std::collections::HashMap;

struct DetectSquares {
    count_map: HashMap<(i32, i32), i32>,
    points: Vec<(i32, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DetectSquares {
    fn new() -> Self {
        DetectSquares {
            count_map: HashMap::new(),
            points: Vec::new(),
        }
    }

    // time complexity: O(1)
    fn add(&mut self, point: Vec<i32>) {
        let x: i32 = point[0];
        let y: i32 = point[1];
        self.count_map
            .entry((x, y))
            .and_modify(|p| *p += 1)
            .or_insert(1);
        self.points.push((x, y));
    }

    // time complexity: O(n)
    fn count(&self, point: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let px: i32 = point[0];
        let py: i32 = point[1];
        for (x, y) in self.points.iter() {
            if (px - x).abs() != (py - y).abs() || px == *x || py == *y {
                continue;
            }
            if !self.count_map.contains_key(&(*x, py)) || !self.count_map.contains_key(&(px, *y)) {
                continue;
            }

            result +=
                self.count_map.get(&(*x, py)).unwrap() * self.count_map.get(&(px, *y)).unwrap();
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::DetectSquares;

    #[test]
    fn test_detect_squares_case_1() {
        // arrange
        let mut detect_squares = DetectSquares::new();

        // act
        detect_squares.add(vec![3, 10]);
        detect_squares.add(vec![11, 2]);
        detect_squares.add(vec![3, 2]);
        let actual1: i32 = detect_squares.count(vec![11, 10]);
        let actual2: i32 = detect_squares.count(vec![14, 8]);
        detect_squares.add(vec![11, 2]);
        let actual3: i32 = detect_squares.count(vec![11, 10]);

        // assert
        assert_eq!(actual1, 1);
        assert_eq!(actual2, 0);
        assert_eq!(actual3, 2);
    }
}
