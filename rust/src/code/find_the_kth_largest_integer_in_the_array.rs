struct Solution {}

impl Solution {
    // NOTE: There is an overflow issue when using u128 so we need to use String in sorting
    // instead.
    pub fn kth_largest_number(mut nums: Vec<String>, k: i32) -> String {
        use std::cmp::Ordering;

        /// NOTE: sort by length and then by value in descending order
        nums.sort_by(|a, b| {
            let v = b.len().cmp(&a.len());
            if v == Ordering::Equal {
                b.cmp(&a)
            } else {
                v
            }
        });
        nums[k as usize - 1].to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_kth_largest_number_case_1() {
        // arrange
        let nums: Vec<String> = vec![
            "3".to_string(),
            "6".to_string(),
            "7".to_string(),
            "10".to_string(),
        ];
        let k: i32 = 4;
        let expected: String = "3".to_string();

        // act
        let actual = Solution::kth_largest_number(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_kth_largest_number_case_2() {
        // arrange
        let nums: Vec<String> = vec![
            "623986800".to_string(),
            "3".to_string(),
            "887298".to_string(),
            "695".to_string(),
            "794".to_string(),
            "6888794705".to_string(),
            "269409".to_string(),
            "59930972".to_string(),
            "723091307".to_string(),
            "726368".to_string(),
            "8028385786".to_string(),
            "378585".to_string(),
        ];
        let k: i32 = 11;
        let expected: String = "695".to_string();

        // act
        let actual = Solution::kth_largest_number(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
