struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let mut interval_len: usize = 0;
        // let target: i32 = nums.iter().fold(0, |acc, x| acc + x);
        let target: i32 = nums.iter().sum::<i32>() - x;
        let mut accu: i32 = 0;
        let mut flag: bool = false;
        let mut l: usize = 0;
        for r in 0..nums.len() {
            accu += nums[r];
            let mut curr_len: usize = r - l + 1;
            while l <= r && accu > target {
                accu -= nums[l];
                curr_len -= 1;
                l += 1;
            }

            if accu == target {
                flag = true;
                interval_len = std::cmp::max(interval_len, curr_len);
            }
        }

        return if flag {
            (nums.len() - interval_len) as i32
        } else {
            -1
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_min_operations_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 1, 4, 2, 3];
        let x: i32 = 5;
        let expected: i32 = 2;

        // act
        let actual = Solution::min_operations(nums, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_operations_case_2() {
        // arrange
        let nums: Vec<i32> = vec![5, 6, 7, 8, 9];
        let x: i32 = 4;
        let expected: i32 = -1;

        // act
        let actual = Solution::min_operations(nums, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_operations_case_3() {
        // arrange
        let nums: Vec<i32> = vec![3, 2, 20, 1, 1, 3];
        let x: i32 = 10;
        let expected: i32 = 5;

        // act
        let actual = Solution::min_operations(nums, x);

        // assert
        assert_eq!(expected, actual);
    }
}
