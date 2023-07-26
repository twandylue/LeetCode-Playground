struct Solution {}

impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut max_area: i32 = 0;
        for y in 0..grid.len() {
            for x in 0..grid[0].len() {
                let area = Self::walk(x, y, &mut grid);
                max_area = std::cmp::max(area, max_area);
            }
        }

        max_area
    }

    fn walk(x: usize, y: usize, grid: &mut Vec<Vec<i32>>) -> i32 {
        let mut area: i32 = 0;
        if x >= grid[0].len() || y >= grid.len() || grid[y][x] == 0 {
            return area;
        }

        area += grid[y][x];
        grid[y][x] = 0;
        area += Self::walk(x + 1, y, grid);
        if let Some(v) = x.checked_sub(1) {
            area += Self::walk(v, y, grid);
        }

        area += Self::walk(x, y + 1, grid);
        if let Some(v) = y.checked_sub(1) {
            area += Self::walk(x, v, grid);
        }

        area
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
