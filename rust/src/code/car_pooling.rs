struct Solution {}

impl Solution {
    // NOTE: time complexity O(nlogn), where n is the number of trips
    pub fn car_pooling(mut trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut min_heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        trips.sort_by(|a, b| a[1].cmp(&b[1]));
        let mut accu: i32 = 0;
        for trip in trips {
            while min_heap
                .peek()
                .filter(|Reverse((end, _))| trip[1] >= *end)
                .is_some()
            {
                if let Some(Reverse((_, remove))) = min_heap.pop() {
                    accu -= remove;
                }
            }
            accu += trip[0];
            min_heap.push(Reverse((trip[2], trip[0])));
            if accu > capacity {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_car_pooling_case_1() {
        // arrange
        let trips: Vec<Vec<i32>> = vec![vec![2, 1, 5], vec![3, 3, 7]];
        let capacity: i32 = 4;
        let expected: bool = false;

        // act
        let actual = Solution::car_pooling(trips, capacity);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_car_pooling_case_2() {
        // arrange
        let trips: Vec<Vec<i32>> = vec![vec![2, 1, 5], vec![3, 3, 7]];
        let capacity: i32 = 5;
        let expected: bool = true;

        // act
        let actual = Solution::car_pooling(trips, capacity);

        // assert
        assert_eq!(expected, actual);
    }
}
