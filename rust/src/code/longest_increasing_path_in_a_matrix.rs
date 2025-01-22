use std::cmp::max;
use std::collections::HashMap;

struct Solution;

impl Solution {
    // time complexity: O(m * n)
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let mut cache: HashMap<(usize, usize), i32> = HashMap::new();
        for r in 0..matrix.len() {
            for c in 0..matrix[r].len() {
                Self::dfs(r, c, &mut cache, -1, &matrix);
            }
        }
        let result: Option<&i32> = cache.values().max();
        match result {
            Some(v) => *v,
            None => 0,
        }
    }

    fn dfs(
        r: usize,
        c: usize,
        cache: &mut HashMap<(usize, usize), i32>,
        prev: i32,
        matrix: &Vec<Vec<i32>>,
    ) -> i32 {
        if r >= matrix.len() || c >= matrix[r].len() || matrix[r][c] <= prev {
            return 0;
        }
        if cache.contains_key(&(r, c)) {
            return cache[&(r, c)];
        }
        let mut up: i32 = 1;
        if r.checked_sub(1).is_some() {
            up = 1 + Self::dfs(r - 1, c, cache, matrix[r][c], matrix);
        }
        let down: i32 = 1 + Self::dfs(r + 1, c, cache, matrix[r][c], matrix);
        let mut left: i32 = 1;
        if c.checked_sub(1).is_some() {
            left = 1 + Self::dfs(r, c - 1, cache, matrix[r][c], matrix);
        }
        let right: i32 = 1 + Self::dfs(r, c + 1, cache, matrix[r][c], matrix);
        let result: i32 = max(up, max(down, max(left, right)));
        cache.insert((r, c), result);
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_longest_increasing_path_case_1() {
        // arrange
        let matrix: Vec<Vec<i32>> = vec![vec![9, 9, 4], vec![6, 6, 8], vec![2, 1, 1]];
        let expected: i32 = 4;

        // act
        let actual = Solution::longest_increasing_path(matrix);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_longest_increasing_path_case_2() {
        // arrange
        let matrix: Vec<Vec<i32>> = vec![vec![3, 4, 5], vec![3, 2, 6], vec![2, 2, 1]];
        let expected: i32 = 4;

        // act
        let actual = Solution::longest_increasing_path(matrix);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_longest_increasing_path_case_3() {
        // arrange
        let matrix: Vec<Vec<i32>> = vec![vec![1]];
        let expected: i32 = 1;

        // act
        let actual = Solution::longest_increasing_path(matrix);

        // assert
        assert_eq!(actual, expected);
    }
}
