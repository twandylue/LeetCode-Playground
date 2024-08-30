struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        use std::cmp::max;
        use std::collections::HashMap;

        let mut count: HashMap<i32, i32> = HashMap::new();
        let mut l: usize = 0;
        let mut result: i32 = 0;
        for r in 0..nums.len() {
            count.entry(nums[r]).and_modify(|x| *x += 1).or_insert(1);
            while let Some(c) = count.get(&nums[r]) {
                if *c > k {
                    count.entry(nums[l]).and_modify(|x| *x -= 1);
                    l += 1;
                } else {
                    break;
                }
            }
            if r >= l {
                result = max(result, (r - l + 1) as i32);
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_subarray_length_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 1, 2, 3, 1, 2];
        let k: i32 = 2;
        let expected: i32 = 6;

        // act
        let actual: i32 = Solution::max_subarray_length(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_subarray_length_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 1, 2, 1, 2, 1, 2];
        let k: i32 = 1;
        let expected: i32 = 2;

        // act
        let actual: i32 = Solution::max_subarray_length(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_subarray_length_case_3() {
        // arrange
        let nums: Vec<i32> = vec![5, 5, 5, 5, 5, 5, 5];
        let k: i32 = 4;
        let expected: i32 = 4;

        // act
        let actual: i32 = Solution::max_subarray_length(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_subarray_length_case_4() {
        // arrange
        let nums: Vec<i32> = vec![1];
        let k: i32 = 1;
        let expected: i32 = 1;

        // act
        let actual: i32 = Solution::max_subarray_length(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
