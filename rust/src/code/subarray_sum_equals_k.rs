struct Solution {}

// [1, 1, 1]
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap;
        let mut pre_accu_map: HashMap<i32, i32> = HashMap::new();
        pre_accu_map.insert(0, 1);
        let mut result: i32 = 0;
        let mut accu: i32 = 0;
        for i in 0..nums.len() {
            accu += nums[i];
            let remain = accu - k;
            if let Some(n) = pre_accu_map.get(&remain) {
                result += n;
            }

            pre_accu_map
                .entry(accu)
                .and_modify(|x| {
                    *x += 1;
                })
                .or_insert(1);
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn subarray_sum_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 1, 1];
        let k: i32 = 2;
        let expected: i32 = 2;

        // act
        let actual = Solution::subarray_sum(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn subarray_sum_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3];
        let k: i32 = 3;
        let expected: i32 = 2;

        // act
        let actual = Solution::subarray_sum(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn subarray_sum_case_3() {
        // arrange
        let nums: Vec<i32> = vec![3, 2, 1, 3];
        let k: i32 = 6;
        let expected: i32 = 2;

        // act
        let actual = Solution::subarray_sum(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn subarray_sum_case_4() {
        // arrange
        let nums: Vec<i32> = vec![-1, -1, 1];
        let k: i32 = 0;
        let expected: i32 = 1;

        // act
        let actual = Solution::subarray_sum(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
