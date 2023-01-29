pub struct Solution {}

impl Solution {
    pub fn missing_number2(nums: Vec<i32>) -> i32 {
        let mut res = nums.len() as i32;
        for i in 0..nums.len() {
            res ^= i as i32 ^ nums[i];
        }

        res
    }

    pub fn missing_number(mut nums: Vec<i32>) -> i32 {
        let length = nums.len() as i32;
        let sum = (1 + length) * length / 2;
        let res = sum - nums.iter().fold(0, |acc, &x| acc + x);

        res
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![3, 0, 1];
        let expected = 2;
        let actual = Solution::missing_number(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let nums = vec![0, 1];
        let expected = 2;
        let actual = Solution::missing_number(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let nums = vec![9, 6, 4, 2, 3, 5, 7, 0, 1];
        let expected = 8;
        let actual = Solution::missing_number(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let nums = vec![3, 0, 1];
        let expected = 2;
        let actual = Solution::missing_number2(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        let nums = vec![0, 1];
        let expected = 2;
        let actual = Solution::missing_number2(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        let nums = vec![9, 6, 4, 2, 3, 5, 7, 0, 1];
        let expected = 8;
        let actual = Solution::missing_number2(nums);

        assert_eq!(expected, actual);
    }
}
