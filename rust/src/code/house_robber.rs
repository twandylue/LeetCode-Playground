pub struct Solution {}

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut rob1: i32 = 0;
        let mut rob2: i32 = 0;

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
        let nums: Vec<i32> = vec![1, 2, 3, 1];
        let expected: i32 = 4;

        // act
        let actual = Solution::rob(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn rob_case_2() {
        // arrange
        let nums: Vec<i32> = vec![2, 7, 9, 3, 1];
        let expected: i32 = 12;

        // act
        let actual = Solution::rob(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
