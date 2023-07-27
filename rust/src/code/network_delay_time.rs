use std::cmp::{max, Reverse};
use std::collections::{BinaryHeap, HashMap, HashSet};

type Distance = i32;
type Vertex = i32;

struct Solution {}

impl Solution {
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut heap: BinaryHeap<Reverse<(Distance, Vertex)>> = BinaryHeap::new();
        let mut visited: HashSet<Vertex> = HashSet::new();
        let mut path: Distance = 0;
        let mut point_map: HashMap<Vertex, Vec<(Distance, Vertex)>> = HashMap::new();
        for item in times {
            point_map
                .entry(item[0])
                .and_modify(|x| x.push((item[2], item[1])))
                .or_insert(vec![(item[2], item[1])]);
        }

        heap.push(Reverse((0, k)));
        while let Some(Reverse((d1, n1))) = heap.pop() {
            if visited.contains(&n1) {
                continue;
            }
            visited.insert(n1);
            path = max(path, d1);

            if let Some(items) = point_map.get(&n1) {
                for item in items {
                    let d2: Distance = item.0;
                    let n2: Vertex = item.1;
                    if visited.contains(&n2) {
                        continue;
                    }
                    heap.push(Reverse((d1 + d2, n2)));
                }
            }
        }

        return if visited.len() == n as usize {
            path
        } else {
            -1
        };
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
