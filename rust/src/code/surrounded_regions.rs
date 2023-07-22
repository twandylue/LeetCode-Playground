struct Solution {}

// NOTE: time complexity: O(n * m), where m = 3 here.
impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        let rows = board.len();
        let cols = board[0].len();

        // Step 1: capture unsurrounded regions (O -> T)
        for r in 0..rows {
            for c in 0..cols {
                // NOTE: borundary check
                if (r == 0 || r == rows - 1) || (c == 0 || c == cols - 1) {
                    Self::dfs(c, r, board);
                }
            }
        }

        // Step 2: capture surrounded regions (O -> X)
        for r in 0..rows {
            for c in 0..cols {
                if board[r][c] == 'O' {
                    board[r][c] = 'X';
                }
            }
        }

        // Step 3: Uncapture unsurrounded regions (T -> O)
        for r in 0..rows {
            for c in 0..cols {
                if board[r][c] == 'T' {
                    board[r][c] = 'O';
                }
            }
        }
    }

    fn dfs(x: usize, y: usize, board: &mut Vec<Vec<char>>) {
        if x >= board[0].len() || y >= board.len() || board[y][x] != 'O' {
            return;
        }

        board[y][x] = 'T';
        Self::dfs(x + 1, y, board);
        if x.checked_sub(1).is_some() {
            Self::dfs(x - 1, y, board);
        }

        Self::dfs(x, y + 1, board);
        if y.checked_sub(1).is_some() {
            Self::dfs(x, y - 1, board);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn solve_case_1() {
        // arrange
        let mut board: Vec<Vec<char>> = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'O', 'O', 'X'],
            vec!['X', 'X', 'O', 'X'],
            vec!['X', 'O', 'X', 'X'],
        ];

        let expected: Vec<Vec<char>> = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'O', 'X', 'X'],
        ];

        // act
        Solution::solve(&mut board);

        // assert
        assert_eq!(expected, board);
    }

    #[test]
    fn solve_case_2() {
        // arrange
        let mut board: Vec<Vec<char>> = vec![vec!['X']];

        let expected: Vec<Vec<char>> = vec![vec!['X']];

        // act
        Solution::solve(&mut board);

        // assert
        assert_eq!(expected, board);
    }
}
