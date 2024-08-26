struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut i: usize = 0;
        let mut j: usize = 1;
        let mut result: Vec<i32> = vec![0; nums.len()];
        for k in 0..nums.len() {
            if nums[k] > 0 {
                result[i] = nums[k];
                i += 2;
            } else {
                result[j] = nums[k];
                j += 2;
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_rearrange_array_case_1() {
        // arrange
        let nums: Vec<i32> = vec![3, 1, -2, -5, 2, -4];
        let expected = vec![3, -2, 1, -5, 2, -4];

        // act
        let actual: Vec<i32> = Solution::rearrange_array(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_rearrange_array_case_2() {
        // arrange
        let nums: Vec<i32> = vec![-1, 1];
        let expected = vec![1, -1];

        // act
        let actual: Vec<i32> = Solution::rearrange_array(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
