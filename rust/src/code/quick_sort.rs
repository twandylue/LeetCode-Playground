struct Solution {}

impl Solution {
    fn quick_sort_recursive(vector: Vec<i32>) -> Vec<i32> {
        if vector.is_empty() {
            return Vec::new();
        }

        let mut output = vector.clone();
        Self::quick_sort_helper(0, output.len() - 1, &mut output);

        return output;
    }

    // pivot is the last item.
    fn quick_sort_helper(left: usize, right: usize, vector: &mut Vec<i32>) {
        if left < right && right < vector.len() {
            let pivot: usize = right;
            println!("original vector: {vector:?}");
            println!("pivot: {pivot}");
            if pivot == 0 {
                return;
            }
            Self::partition(left, pivot - 1, pivot, vector);

            println!("vector: {vector:?}");
            println!("--------");
            Self::quick_sort_helper(left, pivot - 1, vector);
            Self::quick_sort_helper(pivot + 1, right, vector);
        }
    }

    fn partition(mut left: usize, mut right: usize, pivot: usize, vector: &mut Vec<i32>) {
        while left < right && right < vector.len() {
            if vector[left] <= vector[pivot] {
                left += 1;
            } else if vector[left] > vector[pivot] && vector[right] > vector[pivot] {
                right -= 1;
            } else if vector[left] > vector[pivot] && vector[right] <= vector[pivot] {
                Self::swap(left, right, vector);
                left += 1;
                right -= 1;
            }
        }

        if vector[left] > vector[pivot] {
            Self::swap(left, pivot, vector);
        }
    }

    fn swap(l: usize, r: usize, vector: &mut Vec<i32>) {
        let temp = vector[l];
        vector[l] = vector[r];
        vector[r] = temp;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn quick_sort_recursive_case_1() {
        // arrange
        let input = Vec::from([4, 3, 2, 1]);
        let expected = vec![1, 2, 3, 4];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_2() {
        // arrange
        let input = Vec::from([1, 2, 3, 4]);
        let expected = vec![1, 2, 3, 4];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_3() {
        // arrange
        let input = Vec::from([1, 4, 2, 3]);
        let expected = vec![1, 2, 3, 4];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_4() {
        // arrange
        let input = Vec::from([1, 3, 2, 4]);
        let expected = vec![1, 2, 3, 4];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_5() {
        // arrange
        let input = Vec::from([1, 3, 2, 2, 4]);
        let expected = vec![1, 2, 2, 3, 4];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_6() {
        // arrange
        let input = Vec::<i32>::new();
        let expected: Vec<i32> = vec![];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_7() {
        // arrange
        let input = Vec::from([0, 0, 0, 0]);
        let expected = vec![0, 0, 0, 0];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn quick_sort_recursive_case_8() {
        // arrange
        let input = Vec::from([1, 3, 2]);
        let expected = vec![1, 2, 3];

        // act
        let actual = Solution::quick_sort_recursive(input);

        // assert
        assert_eq!(expected, actual);
    }
}
