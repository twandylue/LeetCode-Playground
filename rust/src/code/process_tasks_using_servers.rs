struct Solution {}

impl Solution {
    // NOTE: time complexity O(nlogm), where n is the number of tasks and m is the number of servers
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        use std::cmp::{max, Reverse};
        use std::collections::BinaryHeap;

        let mut result: Vec<i32> = Vec::new();
        let mut avaliable_min_heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        for i in 0..servers.len() {
            avaliable_min_heap.push(Reverse((servers[i], i)));
        }
        let mut unvaliable_min_heap: BinaryHeap<Reverse<(i32, i32, usize)>> = BinaryHeap::new();
        let mut time: i32 = 0;
        for i in 0..tasks.len() {
            time = max(time, i as i32);
            if unvaliable_min_heap.len() > 0 && avaliable_min_heap.len() == 0 {
                if let Some(Reverse((free_time, _, _))) = unvaliable_min_heap.peek() {
                    time = *free_time;
                }
            }
            while let Some(Reverse(t)) = unvaliable_min_heap.peek() {
                if time >= t.0 {
                    if let Some(Reverse((_, weight, idx))) = unvaliable_min_heap.pop() {
                        avaliable_min_heap.push(Reverse((weight, idx)));
                    }
                } else {
                    break;
                }
            }
            if let Some(Reverse((weight, idx))) = avaliable_min_heap.pop() {
                result.push(idx as i32);
                unvaliable_min_heap.push(Reverse((time + tasks[i], weight, idx)));
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_assign_tasks_case_1() {
        // arrange
        let servers: Vec<i32> = vec![3, 3, 2];
        let tasks: Vec<i32> = vec![1, 2, 3, 2, 1, 2];
        let expected: Vec<i32> = vec![2, 2, 0, 2, 1, 2];

        // act
        let actual = Solution::assign_tasks(servers, tasks);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_assign_tasks_case_2() {
        // arrange
        let servers: Vec<i32> = vec![5, 1, 4, 3, 2];
        let tasks: Vec<i32> = vec![2, 1, 2, 4, 5, 2, 1];
        let expected: Vec<i32> = vec![1, 4, 1, 4, 1, 3, 2];

        // act
        let actual = Solution::assign_tasks(servers, tasks);

        // assert
        assert_eq!(actual, expected);
    }
}
