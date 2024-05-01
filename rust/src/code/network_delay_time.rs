struct Solution {}

impl Solution {
    // NOTE: time complexity O(E log V), where E is the number of edges and V is the number of vertices
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        use std::cmp::{max, Reverse};
        use std::collections::{BinaryHeap, HashMap, HashSet};

        type Distance = i32;
        type Vertex = i32;

        let mut min_heap: BinaryHeap<Reverse<(Distance, Vertex)>> = BinaryHeap::new();
        min_heap.push(Reverse((0, k)));
        let mut path: i32 = 0;
        let mut visited: HashSet<Vertex> = HashSet::new();
        let mut graph: HashMap<Vertex, Vec<(Vertex, Distance)>> = HashMap::new();
        for time in times {
            graph
                .entry(time[0])
                .and_modify(|x| x.push((time[1], time[2])))
                .or_insert(vec![(time[1], time[2])]);
        }
        while let Some(Reverse((accu_dis, node))) = min_heap.pop() {
            if visited.contains(&node) {
                continue;
            }
            path = max(path, accu_dis);
            visited.insert(node);
            if let Some(nexts) = graph.get(&node) {
                for (next_node, weight) in nexts {
                    if !visited.contains(next_node) {
                        min_heap.push(Reverse((accu_dis + *weight, *next_node)));
                    }
                }
            }
        }
        if visited.len() == n as usize {
            path
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn network_delay_time_case_1() {
        // arrange
        let times: Vec<Vec<i32>> = vec![vec![2, 1, 1], vec![2, 3, 1], vec![3, 4, 1]];
        let n = 4;
        let k = 2;
        let expected = 2;

        // act
        let actual = Solution::network_delay_time(times, n, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn network_delay_time_case_2() {
        // arrange
        let times: Vec<Vec<i32>> = vec![vec![1, 2, 1]];
        let n = 2;
        let k = 1;
        let expected = 1;

        // act
        let actual = Solution::network_delay_time(times, n, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn network_delay_time_case_3() {
        // arrange
        let times: Vec<Vec<i32>> = vec![vec![1, 2, 1]];
        let n = 2;
        let k = 2;
        let expected = -1;

        // act
        let actual = Solution::network_delay_time(times, n, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn network_delay_time_case_4() {
        // arrange
        let times: Vec<Vec<i32>> = vec![vec![1, 2, 1], vec![2, 3, 2], vec![1, 3, 4]];
        let n = 3;
        let k = 1;
        let expected = 3;

        // act
        let actual = Solution::network_delay_time(times, n, k);

        // assert
        assert_eq!(expected, actual);
    }
}
