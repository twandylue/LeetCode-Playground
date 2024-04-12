struct Solution {}

impl Solution {
    // NOTE: time complexity: O(nlogn), space complexity: O(k)
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        use std::cmp::{max, Reverse};
        use std::collections::BinaryHeap;

        let mut result: i64 = 0;
        let mut pairs: Vec<(i32, i32)> = nums1.into_iter().zip(nums2.into_iter()).collect();
        pairs.sort_by(|a, b| (b.1).cmp(&a.1));
        let mut min_heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum_n1: i64 = 0;
        for (n1, n2) in pairs {
            sum_n1 += n1 as i64;
            min_heap.push(Reverse(n1));
            if min_heap.len() > k as usize {
                if let Some(Reverse(n1_pop)) = min_heap.pop() {
                    sum_n1 -= n1_pop as i64;
                }
            }
            if min_heap.len() == k as usize {
                result = max(result, sum_n1 * n2 as i64);
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn max_score_case_1() {
        // arrange
        let nums1: Vec<i32> = vec![1, 3, 3, 2];
        let nums2: Vec<i32> = vec![2, 1, 3, 4];
        let k: i32 = 3;
        let expected: i64 = 12;

        // act
        let actual = Solution::max_score(nums1, nums2, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_score_case_2() {
        // arrange
        let nums1: Vec<i32> = vec![4, 2, 3, 1, 1];
        let nums2: Vec<i32> = vec![7, 5, 10, 9, 6];
        let k: i32 = 1;
        let expected: i64 = 30;

        // act
        let actual = Solution::max_score(nums1, nums2, k);

        // assert
        assert_eq!(expected, actual);
    }
}
