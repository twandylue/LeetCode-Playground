struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn max_frequency(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut result: i32 = 0;
        nums.sort();
        let mut l: usize = 0;
        let mut accu: i32 = 0;
        for r in 0..nums.len() {
            accu += nums[r];
            let curr_len: i32 = (r - l + 1) as i32;
            if curr_len * nums[r] <= accu + k {
                result = std::cmp::max(result, curr_len);
            } else {
                accu -= nums[l];
                l += 1;
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_frequency_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 4];
        let k: i32 = 5;
        let expected: i32 = 3;

        // act
        let actual = Solution::max_frequency(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_frequency_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 4, 8, 13];
        let k: i32 = 5;
        let expected: i32 = 2;

        // act
        let actual = Solution::max_frequency(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_frequency_case_3() {
        // arrange
        let nums: Vec<i32> = vec![3, 9, 6];
        let k: i32 = 2;
        let expected: i32 = 1;

        // act
        let actual = Solution::max_frequency(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
