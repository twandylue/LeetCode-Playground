use std::cmp::min;
use std::collections::HashSet;

struct Solution;

impl Solution {
    // NOTE: time complexity O(n * m) where n is the number of rows and m is the number of columns
    pub fn closed_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut result: i32 = 0;
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                if !visited.contains(&(r as i32, c as i32)) && grid[r][c] == 0 {
                    result += Self::dfs(r as i32, c as i32, &mut visited, &grid);
                }
            }
        }
        result
    }

    fn dfs(row: i32, col: i32, visited: &mut HashSet<(i32, i32)>, grid: &Vec<Vec<i32>>) -> i32 {
        if row < 0 || col < 0 || row >= grid.len() as i32 || col >= grid[0].len() as i32 {
            return 0;
        }
        if visited.contains(&(row, col)) || grid[row as usize][col as usize] == 1 {
            return 1;
        }
        visited.insert((row, col));
        return min(
            min(
                Self::dfs(row + 1, col, visited, grid),
                Self::dfs(row - 1, col, visited, grid),
            ),
            min(
                Self::dfs(row, col + 1, visited, grid),
                Self::dfs(row, col - 1, visited, grid),
            ),
        );
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_closed_island_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![1, 1, 1, 1, 1, 1, 1, 0],
            vec![1, 0, 0, 0, 0, 1, 1, 0],
            vec![1, 0, 1, 0, 1, 1, 1, 0],
            vec![1, 0, 0, 0, 0, 1, 0, 1],
            vec![1, 1, 1, 1, 1, 1, 1, 0],
        ];
        let expected: i32 = 2;

        // act
        let actual = Solution::closed_island(grid);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_closed_island_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![0, 0, 1, 0, 0],
            vec![0, 1, 0, 1, 0],
            vec![0, 1, 1, 1, 0],
        ];
        let expected: i32 = 1;

        // act
        let actual = Solution::closed_island(grid);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_closed_island_case_3() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![1, 1, 1, 1, 1, 1, 1],
            vec![1, 0, 0, 0, 0, 0, 1],
            vec![1, 0, 1, 1, 1, 0, 1],
            vec![1, 0, 1, 0, 1, 0, 1],
            vec![1, 0, 1, 1, 1, 0, 1],
            vec![1, 0, 0, 0, 0, 0, 1],
            vec![1, 1, 1, 1, 1, 1, 1],
        ];
        let expected: i32 = 2;

        // act
        let actual = Solution::closed_island(grid);

        // assert
        assert_eq!(actual, expected);
    }
}
