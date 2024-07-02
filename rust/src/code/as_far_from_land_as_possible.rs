struct Solution;

impl Solution {
    // NOTE: time complexity: O(n * m), where n is the number of rows and m is the number of columns. space complexity: O(n * m)
    pub fn max_distance(mut grid: Vec<Vec<i32>>) -> i32 {
        use std::cmp::{max, min};
        use std::collections::VecDeque;

        let mut result: i32 = -1;
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                if grid[r][c] == 1 {
                    queue.push_back((r as i32, c as i32));
                }
            }
        }
        let dirs: Vec<(i32, i32)> = Vec::from([(1, 0), (-1, 0), (0, 1), (0, -1)]);
        while let Some((row, col)) = queue.pop_front() {
            result = grid[row as usize][col as usize];
            for (dir_r, dir_c) in dirs.iter() {
                let next_row: i32 = row + dir_r;
                let next_col: i32 = col + dir_c;
                if min(next_row, next_col) >= 0
                    && max(next_row, next_col) < grid.len() as i32
                    && grid[next_row as usize][next_col as usize] == 0
                {
                    queue.push_back((next_row, next_col));
                    grid[next_row as usize][next_col as usize] =
                        grid[row as usize][col as usize] + 1
                }
            }
        }

        if result > 1 {
            result - 1
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_max_distance_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![1, 0, 1], vec![0, 0, 0], vec![1, 0, 1]];
        let expected: i32 = 2;

        // act
        let actual = Solution::max_distance(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_max_distance_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![1, 0, 0], vec![0, 0, 0], vec![0, 0, 0]];
        let expected: i32 = 4;

        // act
        let actual = Solution::max_distance(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
