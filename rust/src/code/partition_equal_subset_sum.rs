use std::collections::HashSet;

struct Solution {}

impl Solution {
    // NOTE: time complexity O(n * sum(nums))
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let s = nums.iter().sum::<i32>();
        if s % 2 == 1 {
            return false;
        }
        let target: i32 = s / 2;

        let mut dp: HashSet<i32> = HashSet::new();
        dp.insert(0);

        for n in nums {
            let mut next_dp: HashSet<i32> = dp.clone();
            for num in dp.iter() {
                next_dp.insert(n + num);
            }
            dp = next_dp;
        }

        return if dp.contains(&target) { true } else { false };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_can_partition_test_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 5, 11, 5];
        let expected = true;

        // act
        let actual = Solution::can_partition(nums);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_can_partition_test_2() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 5];
        let expected = false;

        // act
        let actual = Solution::can_partition(nums);

        // assert
        assert_eq!(actual, expected);
    }
}
