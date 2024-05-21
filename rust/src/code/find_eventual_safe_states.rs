struct Solution;

use std::collections::HashMap;

impl Solution {
    // NOTE: time complexity O(E + V), where E is the number of edges and V is the number of vertices
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let mut safe: HashMap<i32, bool> = HashMap::new();
        let mut result: Vec<i32> = Vec::new();
        for i in 0..graph.len() {
            if Self::dfs(i as i32, &mut safe, &graph) {
                result.push(i as i32);
            }
        }
        result
    }

    fn dfs(node: i32, safe: &mut HashMap<i32, bool>, graph: &Vec<Vec<i32>>) -> bool {
        if let Some(&n) = safe.get(&node) {
            return n;
        } else {
            safe.insert(node, false);
            for neighbor in graph[node as usize].iter() {
                if !Self::dfs(*neighbor, safe, graph) {
                    return false;
                }
            }
            safe.entry(node).and_modify(|x| *x = true);
            return true;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_eventual_safe_nodes_case_1() {
        // arrange
        let graph: Vec<Vec<i32>> = vec![
            vec![1, 2],
            vec![2, 3],
            vec![5],
            vec![0],
            vec![5],
            vec![],
            vec![],
        ];
        let expected: Vec<i32> = vec![2, 4, 5, 6];

        // act
        let actual = Solution::eventual_safe_nodes(graph);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_eventual_safe_nodes_case_2() {
        // arrange
        let graph: Vec<Vec<i32>> =
            vec![vec![1, 2, 3, 4], vec![1, 2], vec![3, 4], vec![0, 4], vec![]];
        let expected: Vec<i32> = vec![4];

        // act
        let actual = Solution::eventual_safe_nodes(graph);

        // assert
        assert_eq!(expected, actual);
    }
}
