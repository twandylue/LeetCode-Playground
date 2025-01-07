struct Solution;

impl Solution {
    // time complexity: O(n * m), where n is the number of rows and m is the number of columns
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        let directions: Vec<(i32, i32)> = vec![
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ];
        for r in 0..board.len() {
            for c in 0..board[r].len() {
                let mut live_neighbors = 0;
                for (dc, dr) in directions.iter() {
                    if r as i32 + dr < 0
                        || r as i32 + dr >= board.len() as i32
                        || c as i32 + dc < 0
                        || c as i32 + dc >= board[r].len() as i32
                        || board[(r as i32 + dr) as usize][(c as i32 + dc) as usize] == 0
                        || board[(r as i32 + dr) as usize][(c as i32 + dc) as usize] == 3
                    {
                        continue;
                    }
                    live_neighbors += 1;
                }
                if board[r][c] == 1 && (live_neighbors < 2 || live_neighbors > 3) {
                    board[r][c] = 2;
                } else if board[r][c] == 1 && (live_neighbors == 2 || live_neighbors == 3) {
                    continue;
                } else if board[r][c] == 0 && live_neighbors == 3 {
                    board[r][c] = 3;
                }
            }
        }

        for r in 0..board.len() {
            for c in 0..board[r].len() {
                if board[r][c] == 2 {
                    board[r][c] = 0;
                }
                if board[r][c] == 3 {
                    board[r][c] = 1;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_game_of_life_case_1() {
        // arrange
        let mut board: Vec<Vec<i32>> =
            vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];
        let expected: Vec<Vec<i32>> =
            vec![vec![0, 0, 0], vec![1, 0, 1], vec![0, 1, 1], vec![0, 1, 0]];

        // act
        Solution::game_of_life(&mut board);

        // assert
        assert_eq!(board, expected);
    }

    #[test]
    fn test_game_of_life_case_2() {
        // arrange
        let mut board: Vec<Vec<i32>> = vec![vec![1, 1], vec![1, 0]];
        let expected: Vec<Vec<i32>> = vec![vec![1, 1], vec![1, 1]];

        // act
        Solution::game_of_life(&mut board);

        // assert
        assert_eq!(board, expected);
    }
}
