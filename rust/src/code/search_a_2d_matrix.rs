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
}
