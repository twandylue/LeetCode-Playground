struct Solution {}

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        use std::collections::BinaryHeap;

        let mut min_heap: BinaryHeap<(i32, Vec<i32>)> = BinaryHeap::new();
        for p in points {
            let dis: i32 = p[0] * p[0] + p[1] * p[1];
            min_heap.push((dis, p));
        }
        while min_heap.len() > k as usize {
            min_heap.pop();
        }
        min_heap.into_iter().map(|(_, x)| x).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn k_closest_case_1() {
        // arrange
        let points: Vec<Vec<i32>> = vec![vec![1, 3], vec![-2, 2]];
        let k = 1;
        let mut expected: Vec<Vec<i32>> = vec![vec![-2, 2]];

        // act
        let mut actual = Solution::k_closest(points, k);

        // arrange
        assert_eq!(
            expected.sort_by(|a, b| b[0].cmp(&a[0])),
            actual.sort_by(|a, b| b[0].cmp(&a[0]))
        );
    }

    #[test]
    fn k_closest_case_2() {
        // arrange
        let points: Vec<Vec<i32>> = vec![vec![3, 3], vec![5, -1], vec![-2, 4]];
        let k = 2;
        let mut expected: Vec<Vec<i32>> = vec![vec![3, 3], vec![-2, 4]];

        // act
        let mut actual = Solution::k_closest(points, k);

        // arrange
        assert_eq!(
            expected.sort_by(|a, b| b[0].cmp(&a[0])),
            actual.sort_by(|a, b| b[0].cmp(&a[0]))
        );
    }

    #[test]
    fn k_closest_case_3() {
        // arrange
        let points: Vec<Vec<i32>> = vec![
            vec![2, 2],
            vec![2, 2],
            vec![2, 2],
            vec![2, 2],
            vec![2, 2],
            vec![2, 2],
            vec![1, 1],
        ];
        let k = 1;
        let mut expected: Vec<Vec<i32>> = vec![vec![1, 1]];

        // act
        let mut actual = Solution::k_closest(points, k);

        // arrange
        assert_eq!(
            expected.sort_by(|a, b| b[0].cmp(&a[0])),
            actual.sort_by(|a, b| b[0].cmp(&a[0]))
        );
    }
}
