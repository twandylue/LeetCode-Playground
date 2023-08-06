use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    // NOTE: Union and Find, time complexity: O(E + V)
    pub fn count_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut parents: Vec<i32> = Vec::new();
        let mut ranks: Vec<i32> = Vec::new();
        let mut result = n;

        for i in 0..n {
            parents.push(i);
            ranks.push(1);
        }

        for edge in edges {
            let s = edge[0];
            let e = edge[1];
            result -= Self::union(s, e, &mut parents, &mut ranks);
        }

        return result;
    }

    fn find(node: i32, parents: &mut Vec<i32>) -> i32 {
        let mut node = node as usize;
        while node != parents[node] as usize {
            node = parents[node] as usize;
            parents[node] = parents[parents[node] as usize];
        }

        return node as i32;
    }

    fn union(n1: i32, n2: i32, parents: &mut Vec<i32>, ranks: &mut Vec<i32>) -> i32 {
        let p1 = Self::find(n1, parents) as usize;
        let p2 = Self::find(n2, parents) as usize;

        if p1 == p2 {
            return 0;
        }

        if ranks[p1] > ranks[p2] {
            parents[p2] = p1 as i32;
            ranks[p1] += ranks[p2];
        } else {
            parents[p1] = p2 as i32;
            ranks[p2] += ranks[p1];
        }

        return 1;
    }

    // NOTE: DFS, time complexity: O(E + V)
    pub fn count_components_dfs(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut adj_nodes: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut count: i32 = 0;
        let prev: i32 = -1;
        for edge in edges {
            let s = edge[0];
            let e = edge[1];
            adj_nodes
                .entry(s)
                .and_modify(|x| x.push(e))
                .or_insert(vec![e]);
            adj_nodes
                .entry(e)
                .and_modify(|x| x.push(s))
                .or_insert(vec![s]);
        }

        for node in 0..n {
            if Self::walk(node, prev, &mut visited, &adj_nodes) {
                count += 1;
            }
        }

        return count;
    }

    fn walk(
        node: i32,
        prev_node: i32,
        visited: &mut HashSet<i32>,
        adj_nodes: &HashMap<i32, Vec<i32>>,
    ) -> bool {
        if visited.contains(&node) {
            return false;
        }

        visited.insert(node);
        if let Some(next_nodes) = adj_nodes.get(&node) {
            for next_node in next_nodes {
                if *next_node == prev_node {
                    continue;
                }

                if Self::walk(*next_node, node, visited, adj_nodes) {
                    continue;
                }

                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn count_components_case_1() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![3, 4]];
        let expected = 2;

        // act
        let actual = Solution::count_components_dfs(n, edges);

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn count_components_case_2() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 4]];
        let expected = 1;

        // act
        let actual = Solution::count_components_dfs(n, edges);

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn count_components_case_3() {
        // arrange
        let n = 6;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![2, 3], vec![4, 5]];
        let expected = 3;

        // act
        let actual = Solution::count_components_dfs(n, edges);

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn count_components_case_4() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![3, 4]];
        let expected = 2;

        // act
        let actual = Solution::count_components(n, edges);

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn count_components_case_5() {
        // arrange
        let n = 5;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 4]];
        let expected = 1;

        // act
        let actual = Solution::count_components(n, edges);

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn count_components_case_6() {
        // arrange
        let n = 6;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![2, 3], vec![4, 5]];
        let expected = 3;

        // act
        let actual = Solution::count_components(n, edges);

        // assert
        assert_eq!(expected, actual)
    }
}
