pub struct Solution {}

impl Solution {
    pub fn combination_sum2(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort();
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut subset: Vec<i32> = Vec::new();
        Self::dfs(0, &candidates, &mut subset, &mut result, target);

        return result;
    }

    fn dfs(
        pos: usize,
        candidates: &Vec<i32>,
        subset: &mut Vec<i32>,
        result: &mut Vec<Vec<i32>>,
        target: i32,
    ) {
        if target == 0 {
            result.push(subset.clone());
        } else if target < 0 {
            return;
        }

        let mut prev: i32 = -1;
        for i in pos..candidates.len() {
            if candidates[i] == prev {
                continue;
            }
            subset.push(candidates[i]);
            Self::dfs(i + 1, candidates, subset, result, target - candidates[i]);
            subset.pop().unwrap();
            prev = candidates[i];
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn combination_sum2_case_1() {
        // arrange
        let candidates: Vec<i32> = vec![10, 1, 2, 7, 6, 1, 5];
        let target: i32 = 8;
        let mut expected: Vec<Vec<i32>> =
            vec![vec![1, 1, 6], vec![1, 2, 5], vec![1, 7], vec![2, 6]];

        // act
        let mut actual = Solution::combination_sum2(candidates, target);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn combination_sum2_case_2() {
        // arrange
        let candidates: Vec<i32> = vec![2, 5, 2, 1, 2];
        let target: i32 = 5;
        let mut expected: Vec<Vec<i32>> = vec![vec![1, 2, 2], vec![5]];

        // act
        let mut actual = Solution::combination_sum2(candidates, target);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }
}
