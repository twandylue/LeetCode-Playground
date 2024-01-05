struct Solution {}

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        use std::collections::HashSet;

        let mut l: usize = 0;
        let mut nums_set: HashSet<i32> = HashSet::new();
        for r in 0..nums.len() {
            if r - l > k as usize {
                nums_set.remove(&nums[l]);
                l += 1
            }
            if nums_set.contains(&nums[r]) {
                return true;
            }
            nums_set.insert(nums[r]);
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_contains_nearby_duplicate_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 1];
        let k: i32 = 3;
        let expected: bool = true;

        // act
        let actual = Solution::contains_nearby_duplicate(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
