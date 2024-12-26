struct Solution {}

impl Solution {
    // NOTE: time complexity O(n), space complexity O(1)
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let mut l: usize = 0;
        let mut r: usize = 0;

        while r < nums.len() - 1 {
            let mut farthest: usize = 0;
            for i in l..(r + 1) {
                farthest = std::cmp::max(farthest, i + nums[i] as usize);
            }
            l = r;
            r = farthest;
            result += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_jump_case_1() {
        // arrange
        let nums: Vec<i32> = vec![2, 3, 1, 1, 4];
        let expected: i32 = 2;

        // act
        let actual = Solution::jump(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_jump_case_2() {
        // arrange
        let nums: Vec<i32> = vec![2, 3, 0, 1, 4];
        let expected: i32 = 2;

        // act
        let actual = Solution::jump(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_jump_case_3() {
        // arrange
        let nums: Vec<i32> = vec![0];
        let expected: i32 = 0;

        // act
        let actual = Solution::jump(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_jump_case_4() {
        // arrange
        let nums: Vec<i32> = vec![3, 4, 3, 2, 5, 4, 3];
        let expected: i32 = 3;

        // act
        let actual = Solution::jump(nums);

        // assert
        assert_eq!(actual, expected);
    }
}
