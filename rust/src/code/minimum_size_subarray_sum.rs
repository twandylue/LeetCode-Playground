struct Solution {}

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut result: i32 = (nums.len() + 1) as i32;
        let mut accu: i32 = 0;
        let mut l: usize = 0;
        for r in 0..nums.len() {
            accu += nums[r];
            while accu >= target {
                result = std::cmp::min(result, (r - l + 1) as i32);
                accu -= nums[l];
                l += 1;
            }
        }

        return if result as usize == nums.len() + 1 {
            0
        } else {
            result
        };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_min_sub_array_len_case_1() {
        // arrange
        let target: i32 = 7;
        let nums: Vec<i32> = vec![2, 3, 1, 2, 4, 3];
        let expected: i32 = 2;

        // act
        let acutal = Solution::min_sub_array_len(target, nums);

        // assert
        assert_eq!(expected, acutal);
    }

    #[test]
    fn test_min_sub_array_len_case_2() {
        // arrange
        let target: i32 = 4;
        let nums: Vec<i32> = vec![1, 4, 4];
        let expected: i32 = 1;

        // act
        let acutal = Solution::min_sub_array_len(target, nums);

        // assert
        assert_eq!(expected, acutal);
    }
}
