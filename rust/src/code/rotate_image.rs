pub struct Solution {}

impl Solution {
    // time complexity: O(n)
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let cols = matrix[0].len();
        // exchange row and col
        for r in 0..matrix.len() {
            for c in r..matrix[r].len() {
                let tmp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = tmp;
            }
        }

        // exchange col
        for r in 0..matrix.len() {
            for c in 0..matrix[r].len() / 2 {
                let tmp = matrix[r][c];
                matrix[r][c] = matrix[r][cols - 1 - c];
                matrix[r][cols - 1 - c] = tmp;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_rotate_case_1() {
        // arrange
        let mut matrix = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
        let expected = vec![vec![7, 4, 1], vec![8, 5, 2], vec![9, 6, 3]];

        // act
        Solution::rotate(&mut matrix);

        // assert
        assert_eq!(expected, matrix);
    }

    #[test]
    fn test_rotate_case_2() {
        // arrange
        let mut matrix = vec![
            vec![5, 1, 9, 11],
            vec![2, 4, 8, 10],
            vec![13, 3, 6, 7],
            vec![15, 14, 12, 16],
        ];
        let expected = vec![
            vec![15, 13, 2, 5],
            vec![14, 3, 4, 1],
            vec![12, 6, 8, 9],
            vec![16, 7, 10, 11],
        ];

        // act
        Solution::rotate(&mut matrix);

        // assert
        assert_eq!(expected, matrix);
    }
}
