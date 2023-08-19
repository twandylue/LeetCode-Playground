use std::cmp::max;

struct Solution {}

type Index = usize;
type Height = i32;

impl Solution {
    // NOTE: time complexity O(n)
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut stack: Vec<(Index, Height)> = Vec::new();
        let mut max_area: i32 = 0;

        for i in 0..heights.len() {
            let mut front_index = i;
            while let Some((_, height)) = stack.last() {
                // NOTE: decreasing order
                if *height > heights[i] {
                    if let Some((index, height)) = stack.pop() {
                        let area: i32 = (i - index) as i32 * height;
                        max_area = max(max_area, area);
                        front_index = index;
                    }
                } else {
                    break;
                }
            }
            stack.push((front_index, heights[i]));
        }

        while let Some((index, height)) = stack.pop() {
            let area: i32 = (heights.len() - 1 - index + 1) as i32 * height;
            max_area = max(max_area, area);
        }

        max_area
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_largest_rectangle_area_case_1() {
        // arrange
        let heights = vec![2, 1, 5, 6, 2, 3];
        let expected = 10;

        // act
        let actual = Solution::largest_rectangle_area(heights);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_largest_rectangle_area_case_2() {
        // arrange
        let heights = vec![2, 4];
        let expected = 4;

        // act
        let actual = Solution::largest_rectangle_area(heights);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_largest_rectangle_area_case_3() {
        // arrange
        let heights = vec![1, 1];
        let expected = 2;

        // act
        let actual = Solution::largest_rectangle_area(heights);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_largest_rectangle_area_case_4() {
        // arrange
        let heights = vec![2, 1, 2];
        let expected = 3;

        // act
        let actual = Solution::largest_rectangle_area(heights);

        // assert
        assert_eq!(actual, expected);
    }
}
