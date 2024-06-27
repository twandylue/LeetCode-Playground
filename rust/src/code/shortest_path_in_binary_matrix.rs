struct Solution {}

impl Solution {
    // NOTE: time complexity is O(n^2), where n is the length of the grid"
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        use std::cmp::{max, min};
        use std::collections::{HashSet, VecDeque};

        let mut queue: VecDeque<(i32, i32, i32)> = VecDeque::from([(0, 0, 1)]);
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        visited.insert((0, 0));
        let dirs: Vec<(i32, i32)> = Vec::from([
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]);
        while let Some((r, c, length)) = queue.pop_front() {
            if min(r, c) < 0 || max(r, c) >= grid.len() as i32 || grid[r as usize][c as usize] == 1
            {
                continue;
            }
            if r == (grid.len() - 1) as i32 && c == (grid.len() - 1) as i32 {
                return length;
            }
            for (dir_r, dir_c) in dirs.iter() {
                let next_r: i32 = r + dir_r;
                let next_c: i32 = c + dir_c;
                if !visited.contains(&(next_r, next_c)) {
                    queue.push_back((next_r, next_c, length + 1));
                    visited.insert((next_r, next_c));
                }
            }
        }
        -1
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_shortest_path_binary_matrix_case_1() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 0]];
        let expected: i32 = 2;

        // act
        let actual = Solution::shortest_path_binary_matrix(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_shortest_path_binary_matrix_case_2() {
        // arrange
        let grid: Vec<Vec<i32>> = vec![vec![0, 0, 0], vec![1, 1, 0], vec![1, 1, 0]];
        let expected: i32 = 4;

        // act
        let actual = Solution::shortest_path_binary_matrix(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
