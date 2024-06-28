use std::cmp::{max, min};
use std::collections::{HashSet, VecDeque};

struct Solution;

impl Solution {
    pub fn shortest_bridge(grid: Vec<Vec<i32>>) -> i32 {
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        let dirs: Vec<(i32, i32)> = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                if grid[r][c] == 1 {
                    Self::dfs(r as i32, c as i32, &dirs, &grid, &mut visited);
                    return Self::bfs(&dirs, &grid, &mut visited);
                }
            }
        }
        -1
    }

    fn dfs(
        row: i32,
        col: i32,
        dirs: &Vec<(i32, i32)>,
        grid: &Vec<Vec<i32>>,
        visited: &mut HashSet<(i32, i32)>,
    ) {
        if min(row, col) < 0
            || max(row, col) >= grid.len() as i32
            || visited.contains(&(row, col))
            || grid[row as usize][col as usize] == 0
        {
            return;
        }
        visited.insert((row, col));
        for (dir_r, dir_c) in dirs.iter() {
            Self::dfs(row + dir_r, col + dir_c, dirs, grid, visited);
        }
    }

    fn bfs(dirs: &Vec<(i32, i32)>, grid: &Vec<Vec<i32>>, visited: &mut HashSet<(i32, i32)>) -> i32 {
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        let mut result: i32 = 0;
        for (r, c) in visited.iter() {
            queue.push_back((*r, *c));
        }
        while queue.len() > 0 {
            for _ in 0..queue.len() {
                if let Some((row, col)) = queue.pop_front() {
                    for (dir_r, dir_c) in dirs {
                        let next_r: i32 = row + dir_r;
                        let next_c: i32 = col + dir_c;
                        if min(next_r, next_c) < 0
                            || max(next_r, next_c) >= grid.len() as i32
                            || visited.contains(&(next_r, next_c))
                        {
                            continue;
                        }
                        if grid[next_r as usize][next_c as usize] == 1 {
                            return result;
                        }
                        queue.push_back((next_r, next_c));
                        visited.insert((next_r, next_c));
                    }
                }
            }
            result += 1;
        }

        -1
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_shortest_bridge_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 0]];
        let expected: i32 = 1;

        // act
        let mut actual = Solution::shortest_bridge(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_shortest_bridge_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 1, 0], vec![0, 0, 0], vec![0, 0, 1]];
        let expected: i32 = 2;

        // act
        let mut actual = Solution::shortest_bridge(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_shortest_bridge_case_3() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![
            vec![1, 1, 1, 1, 1],
            vec![1, 0, 0, 0, 1],
            vec![1, 0, 1, 0, 1],
            vec![1, 0, 0, 0, 1],
            vec![1, 1, 1, 1, 1],
        ];
        let expected: i32 = 1;

        // act
        let mut actual = Solution::shortest_bridge(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
