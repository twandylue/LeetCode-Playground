struct Solution {}

impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut curr_sum: i32 = 0;
        for i in 0..nums.len() {
            if (total - nums[i]) as f32 / 2_f32 == curr_sum as f32 {
                return i as i32;
            }
            curr_sum += nums[i];
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pivot_index_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 7, 3, 6, 5, 6];
        let expected: i32 = 3;

        // act
        let actual = Solution::pivot_index(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_pivot_index_case_2() {
        // arrange
        let nums: Vec<i32> = vec![-1, -1, -1, -1, -1, -1];
        let expected: i32 = -1;

        // act
        let actual = Solution::pivot_index(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
