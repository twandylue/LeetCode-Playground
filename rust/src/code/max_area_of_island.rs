struct Solution {}

use std::cmp::max;
use std::collections::HashSet;

impl Solution {
    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut result: i32 = 0;
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                if grid[i][j] != 0 && !visited.contains(&(i, j)) {
                    let mut area = 0;
                    Self::dfs(i, j, &mut area, &mut visited, &grid);
                    result = max(result, area);
                }
            }
        }
        result
    }

    fn dfs(
        i: usize,
        j: usize,
        area: &mut i32,
        visited: &mut HashSet<(usize, usize)>,
        grid: &Vec<Vec<i32>>,
    ) {
        if i >= grid.len() || j >= grid[i].len() || visited.contains(&(i, j)) || grid[i][j] == 0 {
            return;
        }
        *area += 1;
        visited.insert((i, j));
        Self::dfs(i + 1, j, area, visited, grid);
        if i.checked_sub(1).is_some() {
            Self::dfs(i - 1, j, area, visited, grid);
        }
        Self::dfs(i, j + 1, area, visited, grid);
        if j.checked_sub(1).is_some() {
            Self::dfs(i, j - 1, area, visited, grid);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn max_area_of_island_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            vec![0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ];
        let expected = 6;

        // act
        let actual = Solution::max_area_of_island(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_area_of_island_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 0, 0, 0, 0, 0, 0, 0]];
        let expected = 0;

        // act
        let actual = Solution::max_area_of_island(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
