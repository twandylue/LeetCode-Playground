struct Solution {}

impl Solution {
    // NOTE: time complexity: O(m + n)
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        use std::collections::HashMap;

        let mut nums_map: HashMap<i32, usize> = HashMap::new();
        let mut result: Vec<i32> = vec![-1; nums1.len()];
        let mut stack: Vec<i32> = Vec::new();

        for i in 0..nums1.len() {
            nums_map.insert(nums1[i], i);
        }

        for i in 0..nums2.len() {
            while stack.len() > 0 && stack[stack.len() - 1] < nums2[i] {
                if let Some(n) = stack.pop() {
                    if let Some(index) = nums_map.get(&n) {
                        result[*index] = nums2[i];
                    }
                }
            }
            stack.push(nums2[i])
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_next_greater_element_case_1() {
        // arrange
        let nums1: Vec<i32> = vec![4, 1, 2];
        let nums2: Vec<i32> = vec![1, 3, 4, 2];
        let expected: Vec<i32> = vec![-1, 3, -1];

        // act
        let actual = Solution::next_greater_element(nums1, nums2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_next_greater_element_case_2() {
        // arrange
        let nums1: Vec<i32> = vec![2, 4];
        let nums2: Vec<i32> = vec![1, 2, 3, 4];
        let expected: Vec<i32> = vec![3, -1];

        // act
        let actual = Solution::next_greater_element(nums1, nums2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_next_greater_element_case_3() {
        // arrange
        let nums1: Vec<i32> = vec![1, 3, 5, 2, 4];
        let nums2: Vec<i32> = vec![6, 5, 4, 3, 2, 1, 7];
        let expected: Vec<i32> = vec![7, 7, 7, 7, 7];

        // act
        let actual = Solution::next_greater_element(nums1, nums2);

        // assert
        assert_eq!(expected, actual);
    }
}
