pub struct Solution {}

use std::collections::HashSet;
impl Solution {
    // NOTE: time complexity: O(n * m)
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut count: i32 = 0;
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                if grid[i][j] != '0' && !visited.contains(&(i, j)) {
                    count += 1;
                    Self::dfs(i, j, &mut visited, &grid);
                }
            }
        }
        count
    }

    fn dfs(i: usize, j: usize, visited: &mut HashSet<(usize, usize)>, grid: &Vec<Vec<char>>) {
        if i >= grid.len() || j >= grid[i].len() || grid[i][j] == '0' || visited.contains(&(i, j)) {
            return;
        }
        visited.insert((i, j));
        Self::dfs(i + 1, j, visited, grid);
        if i.checked_sub(1).is_some() {
            Self::dfs(i - 1, j, visited, grid);
        }
        Self::dfs(i, j + 1, visited, grid);
        if j.checked_sub(1).is_some() {
            Self::dfs(i, j - 1, visited, grid);
        }
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let grid: Vec<Vec<char>> = vec![
            vec!['1', '1', '1', '1', '0'],
            vec!['1', '1', '0', '1', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '0', '0', '0'],
        ];
        let expected = 1;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let grid: Vec<Vec<char>> = vec![
            vec!['1', '1', '0', '0', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '1', '0', '0'],
            vec!['0', '0', '0', '1', '1'],
        ];
        let expected = 3;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn t_case_3() {
        // arrange
        let grid: Vec<Vec<char>> = vec![vec!['1'], vec!['1']];
        let expected = 1;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
