struct Solution {}

impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        todo!()
    }

    fn walk(x: usize, y: usize, board: &mut Vec<Vec<char>>) -> bool {
        let mut result: bool = false;
        if x >= board[0].len() || y >= board.len() || board[y][x] == 'X' {
            result = true;
            return result;
        }

        return result;
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
