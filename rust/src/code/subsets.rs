struct Solution {}

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut subset: Vec<i32> = Vec::new();

        Self::dfs(0, &nums, &mut subset, &mut result);

        return result;
    }

    fn dfs(i: usize, nums: &Vec<i32>, subset: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if i >= nums.len() {
            result.push(subset.to_vec());
            return;
        }

        subset.push(nums[i]);
        Self::dfs(i + 1, nums, subset, result);
        subset.pop().unwrap();
        Self::dfs(i + 1, nums, subset, result);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_subsets_case_1() {
        // arrange
        let nums = vec![1, 2, 3];
        let mut expected = vec![
            vec![],
            vec![1],
            vec![2],
            vec![1, 2],
            vec![3],
            vec![1, 3],
            vec![2, 3],
            vec![1, 2, 3],
        ];

        // act
        let mut actual = Solution::subsets(nums);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_subsets_case_2() {
        // arrange
        let nums = vec![0];
        let mut expected = vec![vec![], vec![0]];

        // act
        let mut actual = Solution::subsets(nums);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }
}
