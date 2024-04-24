struct Solution {}

use std::collections::HashSet;

impl Solution {
    // NOTE: time complexity: O(n * m)
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        let mut result: i32 = 0;
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                if grid[i][j] != 0 && !visited.contains(&(i, j)) {
                    result += Self::dfs(i, j, &mut visited, &grid);
                }
            }
        }
        result
    }

    fn dfs(i: usize, j: usize, visited: &mut HashSet<(usize, usize)>, grid: &Vec<Vec<i32>>) -> i32 {
        if i >= grid.len() || j >= grid[i].len() || grid[i][j] == 0 {
            return 1;
        }
        if visited.contains(&(i, j)) {
            return 0;
        }
        visited.insert((i, j));
        let mut result: i32 = 0;
        result += Self::dfs(i + 1, j, visited, grid);
        if i.checked_sub(1).is_some() {
            result += Self::dfs(i - 1, j, visited, grid);
        } else {
            result += 1;
        }
        result += Self::dfs(i, j + 1, visited, grid);
        if j.checked_sub(1).is_some() {
            result += Self::dfs(i, j - 1, visited, grid);
        } else {
            result += 1;
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_island_perimeter_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![0, 1, 0, 0],
            vec![1, 1, 1, 0],
            vec![0, 1, 0, 0],
            vec![1, 1, 0, 0],
        ];
        let expected = 16;

        // act
        let actual = Solution::island_perimeter(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
