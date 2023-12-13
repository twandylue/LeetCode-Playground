struct Solution {}

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        use std::collections::HashSet;

        let mut result: Vec<HashSet<i32>> = vec![HashSet::new(), HashSet::new()];
        let mut nums1_set: HashSet<i32> = HashSet::new();
        let mut nums2_set: HashSet<i32> = HashSet::new();

        for i in 0..nums1.len() {
            nums1_set.insert(nums1[i]);
        }
        for i in 0..nums2.len() {
            nums2_set.insert(nums2[i]);
        }

        for i in 0..nums1.len() {
            if nums2_set.contains(&nums1[i]) {
                continue;
            }
            result[0].insert(nums1[i]);
        }
        for i in 0..nums2.len() {
            if nums1_set.contains(&nums2[i]) {
                continue;
            }
            result[1].insert(nums2[i]);
        }

        vec![
            result[0].clone().into_iter().collect::<Vec<i32>>(),
            result[1].clone().into_iter().collect::<Vec<i32>>(),
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_difference_case_1() {
        // arrange
        let nums1: Vec<i32> = vec![1, 2, 3];
        let nums2: Vec<i32> = vec![2, 4, 6];
        let mut expected: Vec<Vec<i32>> = vec![vec![1, 3], vec![4, 6]];

        // act
        let mut actual = Solution::find_difference(nums1, nums2);

        // assert
        expected.sort();
        actual.sort();
        expected.iter_mut().for_each(|x| x.sort());
        actual.iter_mut().for_each(|x| x.sort());
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_difference_case_2() {
        // arrange
        let nums1: Vec<i32> = vec![1, 2, 3, 3];
        let nums2: Vec<i32> = vec![1, 1, 2, 2];
        let mut expected: Vec<Vec<i32>> = vec![vec![3], vec![]];

        // act
        let mut actual = Solution::find_difference(nums1, nums2);

        // assert
        expected.sort();
        actual.sort();
        expected.iter_mut().for_each(|x| x.sort());
        actual.iter_mut().for_each(|x| x.sort());
        assert_eq!(expected, actual);
    }
}
