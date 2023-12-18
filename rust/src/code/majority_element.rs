struct Solution {}

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;

        let mut num_map: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            num_map.entry(nums[i]).and_modify(|x| *x += 1).or_insert(1);
            if let Some(c) = num_map.get(&nums[i]) {
                if *c > nums.len() as i32 / 2 {
                    return nums[i];
                }
            }
        }

        return 0;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_majority_element_case_1() {
        // arrange
        let nums = vec![3, 2, 3];
        let expected = 3;

        // act
        let actual = Solution::majority_element(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_majority_element_case_2() {
        // arrange
        let nums = vec![2, 2, 1, 1, 1, 2, 2];
        let expected = 2;

        // act
        let actual = Solution::majority_element(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
