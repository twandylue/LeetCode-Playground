struct Solution;

impl Solution {
    // NOTE: time complexity O(n * log(n)) where n is the number of buildings
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, mut ladders: i32) -> i32 {
        use std::collections::BinaryHeap;

        let mut max_heap: BinaryHeap<i32> = BinaryHeap::new();
        for i in 0..heights.len() - 1 {
            let diff: i32 = heights[i + 1] - heights[i];
            if diff < 0 {
                continue;
            }
            bricks -= diff;
            max_heap.push(diff);
            if bricks < 0 {
                if ladders == 0 {
                    return i as i32;
                }
                bricks += max_heap.pop().unwrap();
                ladders -= 1;
            }
        }
        (heights.len() - 1) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_furthest_building_case_1() {
        // arrange
        let heights: Vec<i32> = vec![4, 2, 7, 6, 9, 14, 12];
        let bricks: i32 = 5;
        let ladders: i32 = 1;
        let expected: i32 = 4;

        // act
        let actual = Solution::furthest_building(heights, bricks, ladders);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_furthest_building_case_2() {
        // arrange
        let heights: Vec<i32> = vec![4, 12, 2, 7, 3, 18, 20, 3, 19];
        let bricks: i32 = 10;
        let ladders: i32 = 2;
        let expected: i32 = 7;

        // act
        let actual = Solution::furthest_building(heights, bricks, ladders);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_furthest_building_case_3() {
        // arrange
        let heights: Vec<i32> = vec![14, 3, 19, 3];
        let bricks: i32 = 17;
        let ladders: i32 = 0;
        let expected: i32 = 3;

        // act
        let actual = Solution::furthest_building(heights, bricks, ladders);

        // assert
        assert_eq!(expected, actual);
    }
}
