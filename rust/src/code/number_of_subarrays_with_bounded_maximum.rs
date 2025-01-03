struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
        Self::count_subarrays_with_max_leq(right, &nums)
            - Self::count_subarrays_with_max_leq(left - 1, &nums)
    }

    fn count_subarrays_with_max_leq(number: i32, nums: &Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let mut count: i32 = 0;
        for num in nums {
            if num <= &number {
                count += 1;
            } else {
                count = 0;
            }
            result += count
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_num_subarray_bounded_max_case_1() {
        // arrange
        let nums: Vec<i32> = vec![2, 1, 4, 3];
        let left: i32 = 2;
        let right: i32 = 3;
        let expected: i32 = 3;

        // act
        let actual = Solution::num_subarray_bounded_max(nums, left, right);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_subarray_bounded_max_case_2() {
        // arrange
        let nums: Vec<i32> = vec![2, 9, 2, 5, 6];
        let left: i32 = 2;
        let right: i32 = 8;
        let expected: i32 = 7;

        // act
        let actual = Solution::num_subarray_bounded_max(nums, left, right);

        // assert
        assert_eq!(expected, actual);
    }
}
