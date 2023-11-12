struct Solution {}

impl Solution {
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        let mut max_sum: i32 = nums[0];
        let mut max_curr_sum: i32 = 0;
        let mut min_sum: i32 = nums[0];
        let mut min_curr_sum: i32 = 0;
        let mut total: i32 = 0;
        for i in 0..nums.len() {
            total += nums[i];
            max_curr_sum = std::cmp::max(nums[i], max_curr_sum + nums[i]);
            min_curr_sum = std::cmp::min(nums[i], min_curr_sum + nums[i]);
            max_sum = std::cmp::max(max_sum, max_curr_sum);
            min_sum = std::cmp::min(min_sum, min_curr_sum);
        }

        return if max_sum > 0 {
            std::cmp::max(total - min_sum, max_sum)
        } else {
            max_sum
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_subarray_sum_circular() {
        // arrange
        let nums: Vec<i32> = vec![1, -2, 3, -2];
        let expected: i32 = 3;

        // act
        let actual = Solution::max_subarray_sum_circular(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
