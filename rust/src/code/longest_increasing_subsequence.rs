struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n^2)
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp: Vec<i32> = vec![1; nums.len()];
        for i in (0..nums.len()).rev() {
            for j in (i + 1)..nums.len() {
                if nums[i] < nums[j] {
                    dp[i] = std::cmp::max(dp[i], 1 + dp[j]);
                }
            }
        }

        return dp.into_iter().max().unwrap();
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_length_of_lis_case_1() {
        // arrange
        let nums = vec![10, 9, 2, 5, 3, 7, 101, 18];
        let expected = 4;

        // act
        let actual = Solution::length_of_lis(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_length_of_lis_case_2() {
        // arrange
        let nums = vec![0, 1, 0, 3, 2, 3];
        let expected = 4;

        // act
        let actual = Solution::length_of_lis(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_length_of_lis_case_3() {
        // arrange
        let nums = vec![7, 7, 7, 7, 7, 7, 7];
        let expected = 1;

        // act
        let actual = Solution::length_of_lis(nums);

        // assert
        assert_eq!(actual, expected);
    }
}
