struct Solution {}

impl Solution {
    // [1, 3, 0, 0, 2, 0, 0, 4]
    // [0, 0]
    // [0, 0, 0, 2, 0, 0]
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut count: i64 = 0;
        let mut comb: i64 = 0;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                count += 1;
            } else {
                comb += Self::cal_helper(count);
                count = 0
            }
        }

        comb += Self::cal_helper(count);

        comb
    }

    fn cal_helper(num: i64) -> i64 {
        let mut result = 0;

        if num == 0 {
            return 0;
        }

        for i in 1..num + 1 {
            result += i;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn zero_filled_subarray_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 3, 0, 0, 2, 0, 0, 4];
        let expected: i64 = 6;

        // act
        let actual = Solution::zero_filled_subarray(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn zero_filled_subarray_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0, 0, 0, 2, 0, 0];
        let expected: i64 = 9;

        // act
        let actual = Solution::zero_filled_subarray(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn zero_filled_subarray_case_3() {
        // arrange
        let nums: Vec<i32> = vec![0, 0];
        let expected: i64 = 3;

        // act
        let actual = Solution::zero_filled_subarray(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
