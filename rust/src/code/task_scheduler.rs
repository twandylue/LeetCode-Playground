struct Solution {}

// NOTE:
// 1. heap_pop() => represent for executing
// 2. queue => like a buffer for waiting
// time complexity: O(n)
impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        use std::collections::{BinaryHeap, HashMap, VecDeque};

        let mut time: i32 = 0;
        let mut counter: HashMap<char, i32> = HashMap::new();
        for task in tasks {
            counter.entry(task).and_modify(|x| *x += 1).or_insert(1);
        }
        let mut max_heap: BinaryHeap<i32> = BinaryHeap::new();
        for cnt in counter.values() {
            max_heap.push(*cnt);
        }
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new();
        loop {
            if let Some(c) = max_heap.pop() {
                if c - 1 > 0 {
                    queue.push_back((c - 1, time + n));
                }
            }
            if let Some(&(c, t)) = queue.front() {
                if time >= t {
                    max_heap.push(c);
                    queue.pop_front();
                }
            }
            time += 1;
            if max_heap.len() == 0 && queue.len() == 0 {
                break;
            }
        }

        time
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
