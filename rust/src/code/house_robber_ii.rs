struct Solution {}

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        std::cmp::max(
            std::cmp::max(nums[0], Self::rob_helper(nums[1..].to_vec())),
            Self::rob_helper(nums[..(nums.len() - 1)].to_vec()),
        )
    }

    fn rob_helper(nums: Vec<i32>) -> i32 {
        let mut rob1 = 0;
        let mut rob2 = 0;
        for n in nums {
            let new_rob = std::cmp::max(rob1 + n, rob2);
            rob1 = rob2;
            rob2 = new_rob;
        }

        rob2
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn rob_case_1() {
        // arrange
        let nums: Vec<i32> = vec![2, 3, 2];
        let expected = 3;

        // act
        let actual = Solution::rob(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn rob_case_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 1];
        let expected = 4;

        // act
        let actual = Solution::rob(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn rob_case_3() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3];
        let expected = 3;

        // act
        let actual = Solution::rob(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
