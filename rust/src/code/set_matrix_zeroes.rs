struct Solution {}

impl Solution {
    // NOTE: time complexity O(m*n), space complexity O(m+n)
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut rows = vec![];
        let mut cols = vec![];
        for i in 0..matrix.len() {
            for j in 0..matrix[i].len() {
                if matrix[i][j] == 0 {
                    rows.push(i);
                    cols.push(j);
                }
            }
        }

        for i in 0..matrix.len() {
            for j in 0..matrix[i].len() {
                if rows.contains(&i) || cols.contains(&j) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_set_zeroes_case_1() {
        // arrange
        let mut matrix = vec![vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]];
        let expected = vec![vec![1, 0, 1], vec![0, 0, 0], vec![1, 0, 1]];

        // act
        Solution::set_zeroes(&mut matrix);

        // assert
        assert_eq!(matrix, expected);
    }

    #[test]
    fn test_set_zeroes_case_2() {
        // arrange
        let mut matrix = vec![vec![0, 1, 2, 0], vec![3, 4, 5, 2], vec![1, 3, 1, 5]];
        let expected = vec![vec![0, 0, 0, 0], vec![0, 4, 5, 0], vec![0, 3, 1, 0]];

        // act
        Solution::set_zeroes(&mut matrix);

        // assert
        assert_eq!(matrix, expected);
    }
}
