use std::{cmp, collections::HashSet};

pub struct Solution {}

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut p = 0;
        // let set: HashSet<i32> = HashSet::from_iter(nums); -- OK
        let set: HashSet<i32> = nums.clone().into_iter().collect();
        nums.iter().for_each(|x| {
            let mut num = *x;
            if !set.contains(&(num - 1)) {
                p = 0;
                while set.contains(&num) {
                    p += 1;
                    num += 1;
                }
                res = cmp::max(res, p);
            }
        });

        return res;
    }

    pub fn longest_consecutive2(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let num_set: HashSet<i32> = HashSet::from_iter(nums.clone());
        nums.iter().for_each(|&x| {
            if !num_set.contains(&(x - 1)) {
                let mut count: i32 = 0;
                while num_set.contains(&(x + count)) {
                    count += 1;
                }
                result = cmp::max(result, count);
            }
        });

        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn longest_consecutive_case_1() {
        // arrange
        let input = vec![100, 4, 200, 1, 3, 2];
        let expected = 4;

        // act
        let actual = Solution::longest_consecutive(input);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn longest_consecutive_case_2() {
        // arrange
        let input = vec![1, 2, 3, 4, 5];
        let expected = 5;

        // act
        let actual = Solution::longest_consecutive(input);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn longest_consecutive_case_3() {
        // arrange
        let input = vec![100, 4, 200, 1, 3, 2];
        let expected = 4;

        // act
        let actual = Solution::longest_consecutive2(input);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn longest_consecutive_case_4() {
        // arrange
        let input = vec![1, 2, 3, 4, 5];
        let expected = 5;

        // act
        let actual = Solution::longest_consecutive2(input);

        // assert
        assert_eq!(actual, expected);
    }
}
