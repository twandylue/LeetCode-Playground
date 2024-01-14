struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let mut stack: Vec<(i32, i32)> = Vec::new();
        let mut min_num: i32 = nums[0];
        for i in 0..nums.len() {
            while stack.len() > 0 && stack[stack.len() - 1].0 <= nums[i] {
                stack.pop().unwrap();
            }
            if stack.len() > 0 && nums[i] > stack[stack.len() - 1].1 {
                return true;
            }
            stack.push((nums[i], min_num));
            min_num = std::cmp::min(nums[i], min_num);
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find132pattern_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 4];
        let expected: bool = false;

        // act
        let mut actual = Solution::find132pattern(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find132pattern_case_2() {
        // arrange
        let nums: Vec<i32> = vec![3, 1, 4, 2];
        let expected: bool = true;

        // act
        let mut actual = Solution::find132pattern(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find132pattern_case_3() {
        // arrange
        let nums: Vec<i32> = vec![-1, 3, 2, 0];
        let expected: bool = true;

        // act
        let mut actual = Solution::find132pattern(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
