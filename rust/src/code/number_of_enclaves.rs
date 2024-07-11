use std::collections::HashSet;

struct Solution;

impl Solution {
    // NOTE: time complexity O(n * m) where n is the number of rows and m is the number of columns
    pub fn num_enclaves(grid: Vec<Vec<i32>>) -> i32 {
        let mut total_lands: i32 = 0;
        let mut border_lands: i32 = 0;
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        let dirs: Vec<(i32, i32)> = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                total_lands += grid[r][c];
                if !visited.contains(&(r as i32, c as i32))
                    && grid[r][c] == 1
                    && (r == 0 || r == grid.len() - 1 || c == 0 || c == grid[0].len() - 1)
                {
                    border_lands += Self::dfs(r as i32, c as i32, &dirs, &mut visited, &grid);
                }
            }
        }
        total_lands - border_lands
    }

    fn dfs(
        row: i32,
        col: i32,
        dirs: &Vec<(i32, i32)>,
        visited: &mut HashSet<(i32, i32)>,
        grid: &Vec<Vec<i32>>,
    ) -> i32 {
        if row < 0
            || col < 0
            || row >= grid.len() as i32
            || col >= grid[0].len() as i32
            || visited.contains(&(row, col))
            || grid[row as usize][col as usize] == 0
        {
            return 0;
        }
        let mut result: i32 = 1;
        visited.insert((row, col));
        for (dir_r, dir_c) in dirs.iter() {
            result += Self::dfs(row + dir_r, col + dir_c, dirs, visited, grid);
        }
        result
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn test_num_enclaves_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![0, 0, 0, 0],
            vec![1, 0, 1, 0],
            vec![0, 1, 1, 0],
            vec![0, 0, 0, 0],
        ];
        let expected: i32 = 3;

        // act
        let actual = Solution::num_enclaves(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_enclaves_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![0, 1, 1, 0],
            vec![0, 0, 1, 0],
            vec![0, 0, 1, 0],
            vec![0, 0, 0, 0],
        ];
        let expected: i32 = 0;

        // act
        let actual = Solution::num_enclaves(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
