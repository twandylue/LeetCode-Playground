use std::collections::VecDeque;

struct Solution {}

type X = usize;
type Y = usize;

// NOTE: time complexity: O(n)
impl Solution {
    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut deque: VecDeque<(X, Y)> = VecDeque::new();
        let rows: Y = grid.len();
        let cols: X = grid[0].len();
        let mut time: i32 = 0;
        let mut fresh: i32 = 0;

        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] == 2 {
                    deque.push_back((c, r));
                } else if grid[r][c] == 1 {
                    fresh += 1;
                }
            }
        }

        let dirs: &[(isize, isize)] = &[(-1, 0), (1, 0), (0, 1), (0, -1)];
        while !deque.is_empty() && fresh > 0 {
            for _ in 0..deque.len() {
                if let Some((x, y)) = deque.pop_front() {
                    for (dx, dy) in dirs.iter() {
                        if (*dx < 0 && x == 0) || (*dy < 0 && y == 0) {
                            continue;
                        }

                        let col = (x as isize + *dx) as usize;
                        let row = (y as isize + *dy) as usize;
                        if col >= cols || row >= rows || grid[row][col] != 1 {
                            continue;
                        }

                        grid[row][col] = 2;
                        fresh -= 1;
                        deque.push_back((col, row));
                    }
                }
            }
            time += 1;
        }

        return if fresh == 0 { time } else { -1 };
    }

    pub fn oranges_rotting_2(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut deque: VecDeque<(X, Y)> = VecDeque::new();
        let rows: Y = grid.len();
        let cols: X = grid[0].len();
        let mut time: i32 = 0;
        let mut fresh: i32 = 0;

        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] == 2 {
                    deque.push_back((c, r));
                } else if grid[r][c] == 1 {
                    fresh += 1;
                }
            }
        }

        let dirs: &[(isize, isize)] = &[(-1, 0), (1, 0), (0, 1), (0, -1)];
        while !deque.is_empty() && fresh > 0 {
            for _ in 0..deque.len() {
                if let Some((x, y)) = deque.pop_front() {
                    for (dx, dy) in dirs.iter() {
                        if let (Some(col), Some(row)) =
                            (x.checked_add_signed(*dx), y.checked_add_signed(*dy))
                        {
                            if col >= cols || row >= rows || grid[row][col] != 1 {
                                continue;
                            }

                            grid[row][col] = 2;
                            fresh -= 1;
                            deque.push_back((col, row));
                        }
                    }
                }
            }
            time += 1;
        }

        return if fresh == 0 { time } else { -1 };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn oranges_rotting_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]];
        let expected: i32 = 4;

        // act
        let actual = Solution::oranges_rotting(grid);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn oranges_rotting_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![2, 1, 1], vec![0, 1, 1], vec![1, 0, 1]];
        let expected: i32 = -1;

        // act
        let actual = Solution::oranges_rotting(grid);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn oranges_rotting_case_3() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 2]];
        let expected: i32 = 0;

        // act
        let actual = Solution::oranges_rotting(grid);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn oranges_rotting_case_4() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]];
        let expected: i32 = 4;

        // act
        let actual = Solution::oranges_rotting_2(grid);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn oranges_rotting_case_5() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![2, 1, 1], vec![0, 1, 1], vec![1, 0, 1]];
        let expected: i32 = -1;

        // act
        let actual = Solution::oranges_rotting_2(grid);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn oranges_rotting_case_6() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 2]];
        let expected: i32 = 0;

        // act
        let actual = Solution::oranges_rotting_2(grid);

        // arrange
        assert_eq!(expected, actual);
    }
}
