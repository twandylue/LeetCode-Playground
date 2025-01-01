struct Solution;

impl Solution {
    // time compleixty: O(n)
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut ranges: Vec<(i32, i32)> = Vec::new(); // Stores ranges as (start, end) tuples
        for &num in &nums {
            if let Some((_, end)) = ranges.last_mut() {
                if *end + 1 == num {
                    *end = num; // Extend the current range
                } else {
                    ranges.push((num, num)); // Start a new range
                }
            } else {
                ranges.push((num, num)); // Initialize the first range
            }
        }

        ranges
            .into_iter()
            .map(|(start, end)| {
                if start == end {
                    start.to_string()
                } else {
                    format!("{}->{}", start, end)
                }
            })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_summary_ranges_case_1() {
        // arrange
        let nums: Vec<i32> = vec![0, 1, 2, 4, 5, 7];
        let expected: Vec<String> = vec!["0->2".to_string(), "4->5".to_string(), "7".to_string()];

        // act
        let actual = Solution::summary_ranges(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_summary_ranges_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0, 2, 3, 4, 6, 8, 9];
        let expected: Vec<String> = vec![
            "0".to_string(),
            "2->4".to_string(),
            "6".to_string(),
            "8->9".to_string(),
        ];

        // act
        let actual = Solution::summary_ranges(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
