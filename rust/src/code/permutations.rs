use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        if nums.len() == 1 {
            result.push(nums.clone());
            return result;
        }

        let mut ns = VecDeque::from(nums);
        for _ in 0..ns.len() {
            if let Some(n) = ns.pop_front() {
                let mut perms = Self::permute(ns.clone().into_iter().collect::<Vec<i32>>());

                for perm in perms.iter_mut() {
                    perm.push(n)
                }
                result.append(&mut perms);
                ns.push_back(n)
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn permute_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3];
        let mut expected: Vec<Vec<i32>> = vec![
            vec![1, 2, 3],
            vec![1, 3, 2],
            vec![2, 1, 3],
            vec![2, 3, 1],
            vec![3, 1, 2],
            vec![3, 2, 1],
        ];

        // act
        let mut actual = Solution::permute(nums);

        // arrange
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn permute_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0, 1];
        let mut expected: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 0]];

        // act
        let mut actual = Solution::permute(nums);

        // arrange
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn permute_case_3() {
        // arrange
        let nums: Vec<i32> = vec![1];
        let mut expected: Vec<Vec<i32>> = vec![vec![1]];

        // act
        let mut actual = Solution::permute(nums);

        // arrange
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }
}
