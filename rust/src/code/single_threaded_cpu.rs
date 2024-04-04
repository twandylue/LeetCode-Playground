struct Solution {}

impl Solution {
    pub fn get_order(mut tasks: Vec<Vec<i32>>) -> Vec<i32> {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut result: Vec<i32> = Vec::new();
        let mut min_heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        for i in 0..tasks.len() {
            tasks[i].push(i as i32);
        }
        tasks.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut i: usize = 0;
        let mut time: i32 = tasks[0][0];
        while min_heap.len() > 0 || i < tasks.len() {
            while i < tasks.len() && time >= tasks[i][0] {
                min_heap.push(Reverse((tasks[i][1], tasks[i][2])));
                i += 1;
            }
            if min_heap.len() == 0 {
                time = tasks[i][0];
                continue;
            }
            if let Some(Reverse((proce_time, idx))) = min_heap.pop() {
                time += proce_time;
                result.push(idx);
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_order_case_1() {
        // arrange
        let tasks: Vec<Vec<i32>> = vec![vec![1, 2], vec![2, 4], vec![3, 2], vec![4, 1]];
        let expected: Vec<i32> = vec![0, 2, 3, 1];

        // act
        let actual = Solution::get_order(tasks);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_get_order_case_2() {
        // arrange
        let tasks: Vec<Vec<i32>> =
            vec![vec![7, 10], vec![7, 12], vec![7, 5], vec![7, 4], vec![7, 2]];
        let expected: Vec<i32> = vec![4, 3, 2, 0, 1];

        // act
        let actual = Solution::get_order(tasks);

        // assert
        assert_eq!(expected, actual);
    }
}
