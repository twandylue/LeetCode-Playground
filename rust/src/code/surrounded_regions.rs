struct Solution {}

// NOTE: time complexity: O(n * m)
impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        for r in 0..board.len() {
            for c in 0..board[r].len() {
                if r == 0 || r == board.len() - 1 || c == 0 || c == board[r].len() - 1 {
                    Self::dfs(r, c, board);
                }
            }
        }
        for r in 0..board.len() {
            for c in 0..board[r].len() {
                if board[r][c] == 'O' {
                    board[r][c] = 'X';
                } else if board[r][c] == 'T' {
                    board[r][c] = 'O';
                }
            }
        }
    }

    fn dfs(r: usize, c: usize, board: &mut Vec<Vec<char>>) {
        if r == board.len() || c == board[r].len() || board[r][c] != 'O' {
            return;
        }
        board[r][c] = 'T';
        if r.checked_sub(1).is_some() {
            Self::dfs(r - 1, c, board);
        }
        Self::dfs(r + 1, c, board);
        if c.checked_sub(1).is_some() {
            Self::dfs(r, c - 1, board);
        }
        Self::dfs(r, c + 1, board);
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
