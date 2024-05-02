use std::collections::HashSet;

impl Solution {
    // NOTE: time complexity O(n), where n is the number of cells in the grid
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {
        let mut visited: HashSet<(usize, usize)> = HashSet::new();
        let mut count: i32 = 0;
        for r in 0..grid2.len() {
            for c in 0..grid2[r].len() {
                if grid2[r][c] == 1
                    && !visited.contains(&(r, c))
                    && Self::dfs(r, c, &grid1, &grid2, &mut visited)
                {
                    count += 1;
                }
            }
        }
        count
    }

    fn dfs(
        r: usize,
        c: usize,
        grid1: &Vec<Vec<i32>>,
        grid2: &Vec<Vec<i32>>,
        visited: &mut HashSet<(usize, usize)>,
    ) -> bool {
        if r == grid2.len() || c == grid2[r].len() || visited.contains(&(r, c)) || grid2[r][c] == 0
        {
            return true;
        }
        visited.insert((r, c));
        let mut result: bool = true;
        if grid1[r][c] == 0 {
            result = false;
        }
        result = Self::dfs(r + 1, c, grid1, grid2, visited) && result;
        if r.checked_sub(1).is_some() {
            result = Self::dfs(r - 1, c, grid1, grid2, visited) && result;
        }
        result = Self::dfs(r, c + 1, grid1, grid2, visited) && result;
        if c.checked_sub(1).is_some() {
            result = Self::dfs(r, c - 1, grid1, grid2, visited) && result;
        }
        result
    }
}
