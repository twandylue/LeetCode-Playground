struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        use std::collections::HashMap;

        let mut remain_map: HashMap<i32, i32> = HashMap::from([(0, -1)]);
        let mut total: i32 = 0;
        for i in 0..nums.len() {
            total += nums[i];
            let remain: i32 = total % k;
            if !remain_map.contains_key(&remain) {
                remain_map.insert(remain, i as i32);
            } else if i as i32 - remain_map[&remain] > 1 {
                return true;
            }
        }
        false
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_check_subarray_sum_case_1() {
        // arrange
        let nums: Vec<i32> = vec![23, 2, 4, 6, 7];
        let k: i32 = 6;
        let expected: bool = true;

        // act
        let actual = Solution::check_subarray_sum(nums, k);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_check_subarray_sum_case_2() {
        // arrange
        let nums: Vec<i32> = vec![23, 2, 6, 4, 7];
        let k: i32 = 13;
        let expected: bool = false;

        // act
        let actual = Solution::check_subarray_sum(nums, k);

        // assert
        assert_eq!(actual, expected);
    }
}
