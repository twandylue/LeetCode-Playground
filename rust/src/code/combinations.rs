struct Solution;

impl Solution {
    // time complexity: O(n!)
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut subset: Vec<i32> = Vec::new();
        let mut result: Vec<Vec<i32>> = Vec::new();
        Self::dfs(1, n, k, &mut subset, &mut result);
        result
    }

    fn dfs(num: i32, n: i32, k: i32, subset: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
        if num > n + 1 {
            return;
        }
        if subset.len() == k as usize {
            result.push(subset.clone());
        }
        for i in num..n + 1 {
            subset.push(i);
            Self::dfs(i + 1, n, k, subset, result);
            subset.pop();
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_combine_case_1() {
        // arrange
        let n: i32 = 4;
        let k: i32 = 2;
        let expected: Vec<Vec<i32>> = vec![
            vec![1, 2],
            vec![1, 3],
            vec![1, 4],
            vec![2, 3],
            vec![2, 4],
            vec![3, 4],
        ];

        // act
        let mut actual = Solution::combine(n, k);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_combine_case_2() {
        // arrange
        let n: i32 = 1;
        let k: i32 = 1;
        let expected: Vec<Vec<i32>> = vec![vec![1]];

        // act
        let mut actual = Solution::combine(n, k);

        // arrange
        assert_eq!(expected, actual);
    }
}
