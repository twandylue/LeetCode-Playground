use std::collections::{BinaryHeap, VecDeque};

struct Solution {}

// NOTE:
// 1. heap_pop() => represent for executing
// 2. queue => like a buffer
// time complexity: O(n)
impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut time: usize = 0;
        // let mut task_his: Vec<char> = Vec::new();
        let tasks_accu: Vec<i32> = tasks.iter().fold(vec![0; 26], |mut acc, &c| {
            acc[(c as u8 - b'A') as usize] += 1;

            acc
        });
        let mut heap: BinaryHeap<(i32, char)> = BinaryHeap::new();
        for i in 0..26 {
            if tasks_accu[i] > 0 {
                heap.push((tasks_accu[i], char::from('A' as u8 + i as u8)));
            }
        }

        let mut queue: VecDeque<((i32, char), usize)> = VecDeque::new();

        while !heap.is_empty() || !queue.is_empty() {
            if let Some(h) = heap.pop() {
                if h.0 - 1 > 0 {
                    // NOTE: push back before next round(as time += 1)
                    queue.push_back(((h.0 - 1, h.1), time + n as usize));
                }
                // task_his.push(h.1);
            } else {
                // task_his.push(' ');
            }

            if queue.len() > 0 && time >= queue[0].1 {
                if let Some(q) = queue.pop_front() {
                    heap.push(q.0);
                }
            }

            time += 1;
        }

        // println!("task_his: {task_his:?}");
        // task_his.len() as i32
        time as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn least_interval_case_1() {
        // arrange
        let tasks: Vec<char> = vec!['A', 'A', 'A', 'B', 'B', 'B'];
        let n: i32 = 2;
        let expected: i32 = 8;

        // act
        let actual = Solution::least_interval(tasks, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn least_interval_case_2() {
        // arrange
        let tasks: Vec<char> = vec!['A', 'A', 'A', 'B', 'B', 'B'];
        let n: i32 = 0;
        let expected: i32 = 6;

        // act
        let actual = Solution::least_interval(tasks, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn least_interval_case_3() {
        // arrange
        let tasks: Vec<char> = vec!['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'];
        let n: i32 = 2;
        let expected: i32 = 16;

        // act
        let actual = Solution::least_interval(tasks, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn least_interval_case_4() {
        // arrange
        let tasks: Vec<char> = vec!['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'];
        let n: i32 = 1;
        let expected: i32 = 12;

        // act
        let actual = Solution::least_interval(tasks, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn least_interval_case_5() {
        // arrange
        let tasks: Vec<char> = vec![
            'A', 'A', 'A', 'B', 'B', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        ];
        let n: i32 = 7;
        let expected: i32 = 18;

        // act
        let actual = Solution::least_interval(tasks, n);

        // assert
        assert_eq!(expected, actual);
    }
}
