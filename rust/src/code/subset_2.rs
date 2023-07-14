struct Solution {}

// NOTE: time complexity: O(n2^n)
impl Solution {
    pub fn subsets_with_dup(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut subset: Vec<i32> = Vec::new();
        nums.sort();
        Self::bfs(0, &nums, &mut subset, &mut result);

        result
    }

    fn bfs(mut i: usize, nums: &Vec<i32>, subset: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if i == nums.len() {
            result.push(subset.clone());
            return;
        }

        // NOTE: All subsets that include nums[i]
        subset.push(nums[i]);
        Self::bfs(i + 1, nums, subset, result);
        subset.pop();

        // NOTE: All subsets don't include nums[i]
        while i + 1 < nums.len() && nums[i] == nums[i + 1] {
            i += 1;
        }

        Self::bfs(i + 1, nums, subset, result);
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn subsets_with_dup_case_1() {
        // arrange
        let nums = vec![1, 2, 2];
        let mut expected = vec![
            vec![],
            vec![1],
            vec![1, 2],
            vec![1, 2, 2],
            vec![2],
            vec![2, 2],
        ];

        // act
        let mut actual = Solution::subsets_with_dup(nums);

        // arrange
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn subsets_with_dup_case_2() {
        // arrange
        let nums = vec![0];
        let mut expected = vec![vec![], vec![0]];

        // act
        let mut actual = Solution::subsets_with_dup(nums);

        // arrange
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }
}
