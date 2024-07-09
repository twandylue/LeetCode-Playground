use std::cmp::max;
use std::collections::{HashMap, VecDeque};

struct Solution;

impl Solution {
    // NOTE: time complexity O(n) where n is the number of nodes
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..edges.len() {
            if edges[i] == -1 {
                graph.entry(i as i32).or_insert(vec![]);
            } else {
                graph.entry(i as i32).or_insert(vec![edges[i]]);
            }
        }
        let mut node1_map: HashMap<i32, i32> = HashMap::new();
        let mut node2_map: HashMap<i32, i32> = HashMap::new();
        Self::bfs(node1, &mut node1_map, &graph);
        Self::bfs(node2, &mut node2_map, &graph);

        let mut result: i32 = -1;
        let mut min_dis: i32 = i32::MAX;
        for i in 0..edges.len() {
            let node: i32 = i as i32;
            if node1_map.contains_key(&node) && node2_map.contains_key(&node) {
                if min_dis > max(node1_map[&node], node2_map[&node]) {
                    min_dis = max(node1_map[&node], node2_map[&node]);
                    result = i as i32;
                }
            }
        }
        result
    }

    fn bfs(node: i32, node_map: &mut HashMap<i32, i32>, graph: &HashMap<i32, Vec<i32>>) {
        let mut queue: VecDeque<(i32, i32)> = VecDeque::from([(node, 0)]);
        node_map.insert(node, 0);
        while let Some((n, dis)) = queue.pop_front() {
            for neighbor in graph[&n].iter() {
                if node_map.contains_key(neighbor) {
                    continue;
                }
                node_map.insert(*neighbor, dis + 1);
                queue.push_back((*neighbor, dis + 1));
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_closest_meeting_node_case_1() {
        // arrange
        let edges: Vec<i32> = vec![2, 2, 3, -1];
        let node1: i32 = 0;
        let node2: i32 = 1;
        let expected: i32 = 2;

        // act
        let actual = Solution::closest_meeting_node(edges, node1, node2);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_closest_meeting_node_case_2() {
        // arrange
        let edges: Vec<i32> = vec![1, 2, -1];
        let node1: i32 = 0;
        let node2: i32 = 2;
        let expected: i32 = 2;

        // act
        let actual = Solution::closest_meeting_node(edges, node1, node2);

        // arrange
        assert_eq!(expected, actual);
    }
}
