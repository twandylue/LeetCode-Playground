use std::collections::HashSet;

pub struct Solution {}

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut row_set = HashSet::<(usize, u32)>::new();
        let mut col_set = HashSet::<(usize, u32)>::new();
        let mut sub_box_set = vec![HashSet::<(usize, u32)>::new(); board.len() * board[0].len()];

        for r in 0..board.len() {
            for c in 0..board.len() {
                if let Some(digit) = board[r][c].to_digit(10) {
                    if !row_set.insert((r, digit)) {
                        return false;
                    }
                    if !col_set.insert((c, digit)) {
                        return false;
                    }
                    let index = 3 * (r / 3) + c / 3;
                    if !sub_box_set[index].insert((index, digit)) {
                        return false;
                    }
                }
            }
        }

        true
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    pub fn valid_sudoku_case1() {
        // arrange
        let input = vec![
            vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];
        let expected = true;

        // act
        let actual = Solution::is_valid_sudoku(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    pub fn valid_sudoku_case2() {
        // arrange
        let input = vec![
            vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];
        let expected = false;

        // act
        let actual = Solution::is_valid_sudoku(input);

        // assert
        assert_eq!(expected, actual);
    }
}
