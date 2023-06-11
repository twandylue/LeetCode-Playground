struct Solution {}

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let mut merged_vector: Vec<i32> = Vec::new();
        for v in matrix {
            merged_vector.extend(v);
        }
        let mut l = 0;
        let mut r = merged_vector.len() - 1;
        while l <= r {
            let mid = (l + r) / 2;
            if merged_vector[mid] == target {
                return true;
            } else if merged_vector[mid] > target {
                if mid == 0 {
                    break;
                }
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        false
    }

    pub fn search_matrix2(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let mut bot = 0;
        let mut top = matrix.len() - 1;
        let mut l = 0;
        let mut r = matrix[0].len() - 1;

        while bot <= top {
            let mid = (bot + top) / 2;
            if target > matrix[mid][r] {
                bot = mid + 1;
            } else if target < matrix[mid][0] {
                if mid > 0 {
                    top = mid - 1;
                } else {
                    break;
                }
            } else {
                break;
            }
        }

        if bot > top {
            return false;
        }
        let row = (bot + top) / 2;

        while l <= r {
            let mid = (l + r) / 2;
            if target == matrix[row][mid] {
                return true;
            } else if target > matrix[row][mid] {
                l = mid + 1;
            } else if target < matrix[row][mid] {
                if mid > 0 {
                    r = mid - 1;
                } else {
                    break;
                }
            }
        }

        return false;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn search_matrix_case_1() {
        // arrange
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 3;
        let expected = true;

        // act
        let actual = Solution::search_matrix(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_2() {
        // arrange
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 13;
        let expected = false;

        // act
        let actual = Solution::search_matrix(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_3() {
        // arrange
        let matrix = vec![vec![0]];
        let target = 0;
        let expected = true;

        // act
        let actual = Solution::search_matrix(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_4() {
        // arrange
        let matrix = vec![vec![1]];
        let target = 0;
        let expected = false;

        // act
        let actual = Solution::search_matrix(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_5() {
        // arrange
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 3;
        let expected = true;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_6() {
        // arrange
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        let target = 13;
        let expected = false;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_7() {
        // arrange
        let matrix = vec![vec![0]];
        let target = 0;
        let expected = true;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_8() {
        // arrange
        let matrix = vec![vec![1]];
        let target = 0;
        let expected = false;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_9() {
        // arrange
        let matrix = vec![vec![1]];
        let target = 2;
        let expected = false;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn search_matrix_case_10() {
        // arrange
        let matrix = vec![vec![1], vec![3], vec![5]];
        let target = 3;
        let expected = true;

        // act
        let actual = Solution::search_matrix2(matrix, target);

        // assert
        assert_eq!(expected, actual);
    }
}
