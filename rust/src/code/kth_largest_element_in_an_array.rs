struct Solution {}

impl Solution {
    // NOTE: time complexity O(nlogn)
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::BinaryHeap;

        let heap = BinaryHeap::from(nums);
        let v = heap
            .into_sorted_vec()
            .into_iter()
            .rev()
            .collect::<Vec<i32>>();

        v[k as usize - 1]
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn find_kth_largest_case_1() {
        // arrange
        let nums: Vec<i32> = vec![3, 2, 1, 5, 6, 4];
        let k: i32 = 2;
        let expected: i32 = 5;

        // act
        let actual = Solution::find_kth_largest(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_kth_largest_case_2() {
        // arrange
        let nums: Vec<i32> = vec![3, 2, 3, 1, 2, 4, 5, 5, 6];
        let k: i32 = 4;
        let expected: i32 = 4;

        // act
        let actual = Solution::find_kth_largest(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
