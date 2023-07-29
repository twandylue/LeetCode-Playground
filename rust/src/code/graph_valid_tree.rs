use std::collections::{HashMap, HashSet};

pub struct Solution {}

// NOTE: Time complexity: O(E + V)
impl Solution {
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        if edges.is_empty() && n == 0 {
            return true;
        }

        let mut visited: HashSet<i32> = HashSet::new();
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for edge in edges {
            let s = edge[0];
            let e = edge[1];
            // NOTE: bidirectional way
            graph.entry(s).and_modify(|x| x.push(e)).or_insert(vec![e]);
            graph.entry(e).and_modify(|x| x.push(s)).or_insert(vec![s]);
        }

        return Self::walk(0, -1, &mut visited, &graph) && n == visited.len() as i32;
    }

    fn walk(
        node: i32,
        prev_node: i32,
        visited: &mut HashSet<i32>,
        graph: &HashMap<i32, Vec<i32>>,
    ) -> bool {
        if visited.contains(&node) {
            return false;
        }

        visited.insert(node);
        if let Some(next_nodes) = graph.get(&node) {
            for next_node in next_nodes {
                if *next_node == prev_node {
                    continue;
                }

                if Self::walk(*next_node, node, visited, graph) {
                    continue;
                }
                return false;
            }
        }

        return true;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn valid_tree_case_1() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 4]];
        let expected = true;

        // act
        let actual = Solution::valid_tree(n, edges);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn valid_tree_case_2() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![1, 3], vec![1, 4]];
        let expected = false;

        // act
        let actual = Solution::valid_tree(n, edges);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn valid_tree_case_3() {
        // arrange
        let n = 2;
        let edges: Vec<Vec<i32>> = vec![vec![1, 0]];
        let expected = true;

        // act
        let actual = Solution::valid_tree(n, edges);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn valid_tree_case_4() {
        // arrange
        let n = 2;
        let edges: Vec<Vec<i32>> = vec![];
        let expected = false;

        // act
        let actual = Solution::valid_tree(n, edges);

        // arrange
        assert_eq!(expected, actual);
    }
}
