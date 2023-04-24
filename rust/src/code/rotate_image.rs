pub struct Solution {}

impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let d = matrix.len();
        // exchange row and col
        for y in 0..d {
            for x in y..d {
                let temp = matrix[y][x];
                matrix[y][x] = matrix[x][y];
                matrix[x][y] = temp;
            }
        }

        // exchange col
        for y in 0..d {
            for x in 0..d / 2 {
                let temp = matrix[y][x];
                matrix[y][x] = matrix[y][d - 1 - x];
                matrix[y][d - 1 - x] = temp;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let mut matrix = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
        let expected = vec![vec![7, 4, 1], vec![8, 5, 2], vec![9, 6, 3]];

        // act
        Solution::rotate(&mut matrix);

        // assert
        assert_eq!(expected, matrix);
    }

    #[test]
    fn case_2() {
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
