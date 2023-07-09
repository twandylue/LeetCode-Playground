use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();
        for point in points {
            let distance = point[0] * point[0] + point[1] * point[1];
            heap.push((distance, point));
        }

        while heap.len() > k as usize {
            heap.pop();
        }

        heap.into_iter().map(|(_, point)| point).collect()
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
    // #[ignore]
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
