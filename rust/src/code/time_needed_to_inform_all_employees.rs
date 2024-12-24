struct Solution;

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn num_of_minutes_bfs(
        n: i32,
        head_id: i32,
        manager: Vec<i32>,
        inform_time: Vec<i32>,
    ) -> i32 {
        let mut result: i32 = 0;
        let mut adj: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            adj.entry(manager[i as usize] as usize)
                .or_insert(vec![])
                .push(i as usize);
        }
        let mut queue: VecDeque<(usize, i32)> =
            VecDeque::from(vec![(head_id as usize, inform_time[head_id as usize])]);
        while let Some((node, time)) = queue.pop_front() {
            result = std::cmp::max(result, time);
            if !adj.contains_key(&node) {
                continue;
            }
            for employee in adj[&node].iter() {
                queue.push_back((*employee, time + inform_time[*employee]));
            }
        }
        result
    }

    // Time complexity: O(n)
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let mut result: Vec<i32> = vec![0];
        let mut adj: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            adj.entry(manager[i as usize] as usize)
                .or_insert(vec![])
                .push(i as usize);
        }
        Self::dfs(head_id as usize, 0, &mut result, &adj, &inform_time);
        result[0]
    }

    fn dfs(
        i: usize,
        accu_time: i32,
        result: &mut Vec<i32>,
        adj: &HashMap<usize, Vec<usize>>,
        inform_time: &Vec<i32>,
    ) {
        if inform_time[i] == 0 {
            return;
        }
        result[0] = std::cmp::max(result[0], accu_time + inform_time[i]);
        for employee in adj[&i].iter() {
            Self::dfs(
                *employee,
                accu_time + inform_time[i],
                result,
                adj,
                inform_time,
            );
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_num_of_minutes_case_1() {
        // arrange
        let n: i32 = 1;
        let head_id: i32 = 0;
        let manager: Vec<i32> = vec![-1];
        let inform_time: Vec<i32> = vec![0];
        let expected: i32 = 0;

        // act
        let mut actual = Solution::num_of_minutes(n, head_id, manager, inform_time);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_of_minutes_case_2() {
        // arrange
        let n: i32 = 6;
        let head_id: i32 = 2;
        let manager: Vec<i32> = vec![2, 2, -1, 2, 2, 2];
        let inform_time: Vec<i32> = vec![0, 0, 1, 0, 0, 0];
        let expected: i32 = 1;

        // act
        let mut actual = Solution::num_of_minutes(n, head_id, manager, inform_time);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_of_minutes_case_3() {
        // arrange
        let n: i32 = 6;
        let head_id: i32 = 2;
        let manager: Vec<i32> = vec![2, 2, -1, 2, 2, 2];
        let inform_time: Vec<i32> = vec![0, 0, 1, 0, 0, 0];
        let expected: i32 = 1;

        // act
        let mut actual = Solution::num_of_minutes_bfs(n, head_id, manager, inform_time);

        // assert
        assert_eq!(expected, actual);
    }
}
