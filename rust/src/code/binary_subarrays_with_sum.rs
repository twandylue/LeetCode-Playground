struct Solution;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        return Self::helper(&nums, goal) - Self::helper(&nums, goal - 1);
    }

    fn helper(nums: &Vec<i32>, x: i32) -> i32 {
        if x < 0 {
            return 0;
        }
        let mut l: usize = 0;
        let mut curr: i32 = 0;
        let mut result: i32 = 0;
        for r in 0..nums.len() {
            curr += nums[r];
            while curr > x {
                curr -= nums[l];
                l += 1;
            }
            if r >= l {
                result += (r - l + 1) as i32;
            }
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_num_subarrays_with_sum_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 0, 1, 0, 1];
        let goal: i32 = 2;
        let expected: i32 = 4;

        // act
        let actual = Solution::num_subarrays_with_sum(nums, goal);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_subarrays_with_sum_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0, 0, 0, 0, 0];
        let goal: i32 = 0;
        let expected: i32 = 15;

        // act
        let actual = Solution::num_subarrays_with_sum(nums, goal);

        // assert
        assert_eq!(expected, actual);
    }
}
