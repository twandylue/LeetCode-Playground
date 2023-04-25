pub struct Solution {}

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::<i32>::new();
        let width = matrix[0].len();
        let height = matrix.len();
        let mut x_s = 0;
        let mut x_e = width - 1;
        let mut y_s = 0;
        let mut y_e = height - 1;

        while x_s <= x_e && y_s <= y_e {
            // left -> right
            for i in x_s..=x_e {
                result.push(matrix[y_s][i])
            }
            y_s += 1;

            // up -> down
            for i in y_s..=y_e {
                result.push(matrix[i][x_e])
            }
            if let None = x_e.checked_sub(1) {
                break;
            }
            x_e -= 1;

            // right -> left
            if y_s <= y_e {
                for i in (x_s..=x_e).rev() {
                    result.push(matrix[y_e][i])
                }
            }
            if let None = y_e.checked_sub(1) {
                break;
            }
            y_e -= 1;

            // down -> up
            if x_s <= x_e {
                for i in (y_s..=y_e).rev() {
                    result.push(matrix[i][x_s])
                }
            }
            x_s += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let matrix = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
        let expected = vec![1, 2, 3, 6, 9, 8, 7, 4, 5];

        // act
        let actual = Solution::spiral_order(matrix);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let matrix = vec![vec![1, 2, 3, 4], vec![5, 6, 7, 8], vec![9, 10, 11, 12]];
        let expected = vec![1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7];

        // act
        let actual = Solution::spiral_order(matrix);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        // arrange
        let matrix = vec![vec![1]];
        let expected = vec![1];

        // act
        let actual = Solution::spiral_order(matrix);

        // assert
        assert_eq!(expected, actual);
    }
}
