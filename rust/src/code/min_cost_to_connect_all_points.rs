use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};

struct Solution {}

type Distance = i32;
type NodeIndex = usize;

impl Solution {
    // NOTE: time complexity O((n^2)logn)
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let mut cost = 0;
        let mut adj_nodes: HashMap<NodeIndex, Vec<(Distance, NodeIndex)>> = HashMap::new();
        let mut min_heap: BinaryHeap<Reverse<(Distance, NodeIndex)>> = BinaryHeap::new();
        let mut visited: HashSet<NodeIndex> = HashSet::new();

        for i in 0..points.len() {
            let x1: i32 = points[i][0];
            let y1: i32 = points[i][1];
            for j in i + 1..points.len() {
                let x2: i32 = points[j][0];
                let y2: i32 = points[j][1];
                let d: i32 = (x1 - x2).abs() + (y1 - y2).abs();
                adj_nodes
                    .entry(i)
                    .and_modify(|x| x.push((d, j)))
                    .or_insert(vec![(d, j)]);
                adj_nodes
                    .entry(j)
                    .and_modify(|x| x.push((d, i)))
                    .or_insert(vec![(d, i)]);
            }
        }

        // NOTE: init for min heap
        min_heap.push(Reverse((0, 0)));
        while visited.len() != points.len() {
            if let Some(Reverse(item)) = min_heap.pop() {
                if visited.contains(&item.1) {
                    continue;
                }
                visited.insert(item.1);
                cost += item.0;

                if let Some(nodes) = adj_nodes.get(&item.1) {
                    for node in nodes {
                        if visited.contains(&node.1) {
                            continue;
                        }
                        min_heap.push(Reverse(*node));
                    }
                }
            }
        }

        cost
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn min_cost_connect_points_case_1() {
        // arrange
        let points: Vec<Vec<i32>> =
            vec![vec![0, 0], vec![2, 2], vec![3, 10], vec![5, 2], vec![7, 0]];
        let expected = 20;

        // act
        let actual = Solution::min_cost_connect_points(points);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_cost_connect_points_case_2() {
        // arrange
        let points: Vec<Vec<i32>> = vec![vec![3, 12], vec![-2, 5], vec![-4, 1]];
        let expected = 18;

        // act
        let actual = Solution::min_cost_connect_points(points);

        // assert
        assert_eq!(expected, actual);
    }
}
